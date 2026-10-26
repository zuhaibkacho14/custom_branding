(function () {
    const BRANDING_URL = '/ws_dynamic_branding/branding_data';

    function toDataUri(base64Value, mimeType = 'image/png') {
        if (!base64Value) {
            return '';
        }
        if (base64Value.startsWith('data:')) {
            return base64Value;
        }
        return `data:${mimeType};base64,${base64Value}`;
    }

    function updateFavicon(data) {
        const faviconValue = data.brand_favicon ? toDataUri(data.brand_favicon, 'image/png') : '';
        let link = document.querySelector('link[rel="icon"]');
        if (!link) {
            link = document.createElement('link');
            link.rel = 'icon';
            document.head.appendChild(link);
        }
        if (faviconValue) {
            link.href = faviconValue;
        }
    }

    function updateDocumentTitle(data) {
        const brandName = data.brand_short_name || data.brand_name || 'Odoo';
        document.title = brandName;
    }

    function updateLoginBranding(data) {
        const loginLogo = document.querySelector('.oe_login_logo, .o_login_logo, .o_auth_logo, img[alt*="logo"], .ws_brand_logo_login');
        if (data.enable_login_branding && data.brand_login_logo) {
            const finalUrl = toDataUri(data.brand_login_logo, 'image/png');
            if (loginLogo) {
                loginLogo.src = finalUrl;
            }
            const loginTitle = document.querySelector('.oe_login_form .text-center, .o_login_title, .o_login_form h1');
            if (loginTitle) {
                loginTitle.textContent = data.brand_login_title || 'Welcome back';
            }
            const loginText = document.querySelector('.oe_login_form .text-muted, .o_login_subtitle');
            if (loginText) {
                loginText.textContent = data.brand_login_subtitle || 'Log in to continue to your workspace.';
            }
        }
    }

    function updateBackendBranding(data) {
        if (!data.enable_backend_branding) {
            return;
        }
        const brandLogo = data.brand_backend_logo || data.brand_logo;
        if (brandLogo) {
            const targets = document.querySelectorAll(
                '.o_branding_logo, .o_main_navbar .o_menu_brand img, .o_menu_brand img, .o_app_website .o_logo, .o_web_client .o_menu_brand img, .ws_backend_brand_logo'
            );
            targets.forEach((el) => {
                el.src = toDataUri(brandLogo, 'image/png');
            });
        }
        const appNameTargets = document.querySelectorAll('.o_app_name, .o_brand_name, .o_main_navbar .o_menu_brand span');
        appNameTargets.forEach((el) => {
            el.textContent = data.brand_short_name || data.brand_name || 'Odoo';
        });
    }

    function applyBranding(data) {
        if (!data) {
            return;
        }
        updateDocumentTitle(data);
        updateFavicon(data);
        updateBackendBranding(data);
        updateLoginBranding(data);
        const themeColor = data.brand_primary_color || '#875A7B';
        document.documentElement.style.setProperty('--ws-brand-primary', themeColor);
        document.documentElement.style.setProperty('--ws-brand-primary-rgb', themeColor.replace('#', ''));
    }

    function loadBranding() {
        fetch(BRANDING_URL, {
            method: 'GET',
            credentials: 'same-origin',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'application/json',
            },
        })
            .then((response) => response.ok ? response.json() : {})
            .then((data) => applyBranding(data))
            .catch(() => {});
    }

    document.addEventListener('DOMContentLoaded', loadBranding);
    window.addEventListener('load', loadBranding);
    window.setInterval(loadBranding, 600000);
})();
