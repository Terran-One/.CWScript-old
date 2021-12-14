// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "CWScript",
  tagline: "A new way to write dApps on Terra.",
  url: "https://cwscript.terran.one/",
  baseUrl: "/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",
  organizationName: "terran-one", // Usually your GitHub org/user name.
  projectName: "cwscript", // Usually your repo name.

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          editUrl:
            "https://github.com/terran-one/cwscript-docs/edit/main/website/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: "CWScript",
        logo: {
          alt: "CWSCript Logo",
          src: "img/logo.svg",
        },
        items: [
          {
            type: "doc",
            docId: "tutorial/intro",
            position: "left",
            label: "Tutorial",
          },
          {
            type: "doc",
            docId: "manual/intro",
            position: "left",
            label: "Docs",
          },
          {
            type: "doc",
            docId: "tools/intro",
            position: "left",
            label: "Tooling",
          },
          {
            type: "doc",
            docId: "devguide/intro",
            position: "left",
            label: "Developer Guide",
          },
          {
            href: "https://cwscript.terran.one/demo",
            label: "Playground",
          },
          {
            href: "https://github.com/terran-one/cwscript",
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Docs",
            items: [
              {
                label: "Tutorial",
                to: "/docs/intro",
              },
            ],
          },
          {
            title: "Community",
            items: [
              {
                label: "Stack Overflow",
                href: "https://stackoverflow.com/questions/tagged/docusaurus",
              },
              {
                label: "Discord",
                href: "https://discordapp.com/invite/docusaurus",
              },
              {
                label: "Twitter",
                href: "https://twitter.com/docusaurus",
              },
            ],
          },
          {
            title: "More",
            items: [
              {
                label: "Blog",
                to: "/blog",
              },
              {
                label: "GitHub",
                href: "https://github.com/terran-one/cwscript",
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Terran One, Inc.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
