export default {
  theme: "blog",
  srcDir: "blag",
  plugins: ["blog"],
  title: "bageljr.com",
  description: "It's my website!",
  blog: { root: "/posts/" },
  nav: [
    { text: "Homepage", link: "/index.html", icon: "czs-home-l" },
    {
      text: "Categories",
      link: "/categories/index.html",
      icon: "czs-category-l",
    },
    { text: "Tags", link: "/tags/index.html", icon: "czs-tag-l" },
    { text: "About", link: "/about/index.html", icon: "czs-about-l" },
    { text: "Archives", link: "/archives/index.html", icon: "czs-box-l" },
    { text: "Friends", link: "/links/index.html", icon: "czs-link-l" },
  ],
};
