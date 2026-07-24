/**
 * Affiliate & Outbound Link Manager for "No More Everyday Problems"
 * Automatically formats product links, cleans up placeholder tags,
 * and allows dynamic affiliate ID configuration.
 */

(function () {
  const STORAGE_KEY = "nmep_affiliate_id";
  const DEFAULT_TAG = ""; // Leave empty if user doesn't have an affiliate tag

  const getAffiliateId = () => {
    return localStorage.getItem(STORAGE_KEY) || DEFAULT_TAG;
  };

  const setAffiliateId = (tag) => {
    if (tag) {
      localStorage.setItem(STORAGE_KEY, tag.trim());
    } else {
      localStorage.removeItem(STORAGE_KEY);
    }
    cleanAndFormatLinks();
  };

  const cleanAndFormatLinks = () => {
    const affiliateTag = getAffiliateId();
    const links = document.querySelectorAll("a[href*='amazon.com'], a[href*='YOURID-20']");

    links.forEach((link) => {
      let href = link.getAttribute("href");

      if (!href) return;

      if (affiliateTag) {
        // Replace placeholder tag with real tag
        href = href.replace(/tag=[^&]+/g, `tag=${affiliateTag}`).replace(/YOURID-20/g, affiliateTag);
      } else {
        // Strip out YOURID-20 placeholder cleanly so links are valid direct/search links
        href = href.replace(/[?&]tag=YOURID-20/g, "").replace(/YOURID-20/g, "");
      }

      link.setAttribute("href", href);
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener noreferrer");
    });
  };

  // Expose global controller
  window.NMEP_Affiliate = {
    getTag: getAffiliateId,
    setTag: setAffiliateId,
    formatAll: cleanAndFormatLinks
  };

  // Run on DOM load
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", cleanAndFormatLinks);
  } else {
    cleanAndFormatLinks();
  }
})();
