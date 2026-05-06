# RedBooking — Frontend Template System

A complete, production-grade frontend template for a bus booking platform.
Built with HTML5, CSS3, Bootstrap 5, and Vanilla JavaScript. No backend, no build step.

## Folder structure

```
redbooking/
├── pages/
│   ├── index.html       # Home — hero search, popular routes, offers, features, app banner
│   ├── listing.html     # Bus listing — search summary, filters, results, sorting
│   ├── seats.html       # Seat selection — interactive seat map, boarding/dropping points
│   ├── booking.html     # Passenger details + summary
│   ├── payment.html     # Payment (UPI / Card / Net Banking / Wallet) with tabs
│   ├── auth.html        # Login / Signup with split layout + social auth
│   └── bookings.html    # My bookings + profile
├── css/
│   └── styles.css       # Full design system (tokens, components, utilities)
├── js/
│   └── script.js        # All interactions (mobile menu, seats, tabs, filters, validation)
└── assets/              # (empty — drop logos / images here)
```

## How to use

Open `pages/index.html` in your browser. All pages are linked together
(Home → Listing → Seats → Booking → Payment → Bookings, plus Auth).

## Design system

- **Primary:** `#D84E55` (red), with full state palette in `:root`
- **Typography:** Inter (Google Fonts), 8px spacing grid
- **Components:** buttons (primary/outline/ghost/light), cards, forms,
  filter pills, seat grid, payment tabs, status badges, footer
- **Icons:** Bootstrap Icons (CDN)
- **Responsive:** mobile / tablet / desktop breakpoints throughout

## Interactions (vanilla JS)

- Mobile hamburger menu toggle
- From / To swap on hero search
- Filter time pills + sort pills toggling
- Price range slider with live label
- **Seat selection:** click to toggle, live fare summary (count, seats, total)
- Boarding / dropping point selection (single-active)
- Payment method tab switching (UPI / Card / Netbank / Wallet)
- Login / Signup tab switching with form swap
- Simple required-field validation with redirect to next step

No frameworks, no dependencies beyond Bootstrap & Bootstrap Icons CDN.
