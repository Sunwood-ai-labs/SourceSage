import { defineConfig } from "vitepress";

const repo = "https://github.com/Sunwood-ai-labs/SourceSage";

export default defineConfig({
  title: "SourceSage",
  description:
    "Repository analysis CLI that turns source trees into AI-friendly markdown documentation.",
  base: "/SourceSage/",
  cleanUrls: true,
  lastUpdated: true,
  head: [
    ["link", { rel: "icon", type: "image/svg+xml", href: "/logo.svg" }],
    ["meta", { property: "og:type", content: "website" }],
    ["meta", { property: "og:title", content: "SourceSage" }],
    [
      "meta",
      {
        property: "og:description",
        content:
          "Repository analysis CLI that turns source trees into AI-friendly markdown documentation.",
      },
    ],
    [
      "meta",
      {
        property: "og:image",
        content: "https://sunwood-ai-labs.github.io/SourceSage/og-card.svg",
      },
    ],
  ],
  locales: {
    root: {
      label: "English",
      lang: "en-US",
      themeConfig: {
        logo: "/logo.svg",
        nav: [
          { text: "Guide", link: "/guide/getting-started" },
          { text: "CLI", link: "/guide/cli" },
          { text: "日本語", link: "/ja/" },
          { text: "GitHub", link: repo },
        ],
        sidebar: [
          {
            text: "Guide",
            items: [
              { text: "Getting Started", link: "/guide/getting-started" },
              { text: "CLI Reference", link: "/guide/cli" },
              { text: "Output Guide", link: "/guide/output" },
              { text: "Troubleshooting", link: "/guide/troubleshooting" },
            ],
          },
        ],
        editLink: {
          pattern: `${repo}/edit/main/docs/:path`,
          text: "Edit this page on GitHub",
        },
        socialLinks: [{ icon: "github", link: repo }],
        search: { provider: "local" },
        footer: {
          message: "Released under the MIT License.",
          copyright: "Copyright © Sunwood AI Labs",
        },
      },
    },
    ja: {
      label: "日本語",
      lang: "ja-JP",
      link: "/ja/",
      themeConfig: {
        logo: "/logo.svg",
        nav: [
          { text: "ガイド", link: "/ja/guide/getting-started" },
          { text: "CLI", link: "/ja/guide/cli" },
          { text: "English", link: "/" },
          { text: "GitHub", link: repo },
        ],
        sidebar: [
          {
            text: "ガイド",
            items: [
              { text: "はじめに", link: "/ja/guide/getting-started" },
              { text: "CLI リファレンス", link: "/ja/guide/cli" },
              { text: "出力ガイド", link: "/ja/guide/output" },
              { text: "トラブルシューティング", link: "/ja/guide/troubleshooting" },
            ],
          },
        ],
        editLink: {
          pattern: `${repo}/edit/main/docs/:path`,
          text: "GitHub でこのページを編集",
        },
        socialLinks: [{ icon: "github", link: repo }],
        search: { provider: "local" },
        footer: {
          message: "MIT License で公開しています。",
          copyright: "Copyright © Sunwood AI Labs",
        },
      },
    },
  },
});
