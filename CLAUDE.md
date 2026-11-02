# DOTRBA Masterlist: notes for Claude

The owner edits this site from **several Claude chats and projects**, often on the same day.
Each chat only knows its own conversation, so these rules are what keep one chat from undoing
another's work. Read them before changing anything.

Live site: https://asrialbaker.github.io/dotrba-masterlist/ (GitHub Pages, branch `main`).

## Pages

| Page | File | How it's edited |
| --- | --- | --- |
| DOTRBA Masterlist | `index.html` | By hand |
| Devices by others, dotRBA compatible | `devices-by-others/index.html` | By hand |
| Devices developed by dotmod, and collabs | `dotaio-by-dotmod/index.html` | **Generated. Never edit by hand** |

## The dotmod devices page is generated

`dotaio-by-dotmod/index.html` is built by `tools/dotaio/build.py`. Any hand edit to the HTML
is wiped the next time someone runs the builder. To change that page:

1. Edit the source:
   - Cards, sections, photos, colours, notes and dates: the `SECTIONS` list in `tools/dotaio/build.py`.
   - The "Browse the collections" doors in its header: `tools/dotaio/doors.html`.
   - Page text, hero stats, search/SEO tags and page-only CSS: also in `build.py`.
2. Run from the repo root: `python3 tools/dotaio/build.py .`
3. Check `git diff dotaio-by-dotmod/index.html` shows only the changes you meant.
4. Commit the source and the generated HTML together.

If you find hand edits in the HTML that aren't in `build.py` or `doors.html` (someone skipped
these rules), copy them into the source **before** rebuilding.

## Shared styles

The builder copies the whole `<style>` block, the profile links and the lightbox from
`index.html` into the dotmod page. So:

- Any CSS added to `index.html` also applies to the dotmod page. Give new classes specific
  names. Example: the masterlist's red ribbon is `.ribbon`; the dotmod page's brass ribbon is
  `.soon-ribbon`. They once collided and clipped the text.
- After changing `index.html` styles, rebuild the dotmod page and check that it still looks right.

## Collection doors

The "Browse the collections" block (three doors) appears on all three pages. Its counts
(for example "50 RBAs · 6 adapters", "22 models & editions", "20 devices · 5 prototypes")
are typed by hand on `index.html` and `devices-by-others/index.html`. On the dotmod page the
models count is filled in from the cards. When a count changes, update it on every page.

## Photos

- Store photos in `images/`, not as links to other sites (those break or get blocked).
- 900 × 900 px square JPEG, quality about 88–90, cropped close to the device.
- A card shows one big photo (photo 1, the "hero") and three thumbnails (photos 2–4).
- Exception: cards in the **AIO dot platform** section of `devices-by-others/index.html` have
  six thumbnails in two rows (photos 2–7). That section has `data-thumbs="6"`; the shared
  gallery script `dotaio-by-dotmod/dotaio.js` reads it (default 3). Add photos 5–7 as more
  `<img class="shot-src" … hidden>` lines in the card's `.well`; empty slots show as grey boxes.
- Name them by card, for example `dotaio-se-1.jpg` … `dotaio-se-4.jpg`.

## Publishing

1. `git pull` on `main` first, because other chats push here too.
2. Work on a new branch, then open a pull request with the REST API (GraphQL is blocked):
   `gh api repos/asrialbaker/dotrba-masterlist/pulls -f title=… -f head=<branch> -f base=main -F body=@body.md`
3. Merge it: `gh api -X PUT repos/asrialbaker/dotrba-masterlist/pulls/<n>/merge -f merge_method=merge`
4. Wait for the "pages build and deployment" run to succeed:
   `gh api "repos/asrialbaker/dotrba-masterlist/actions/runs?per_page=1"`

## Search engines

Every page has a canonical URL, Open Graph/Twitter tags and schema.org data in its `<head>`.
Add new pages to `sitemap.xml`.
