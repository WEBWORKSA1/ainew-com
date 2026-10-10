/* AiNew.com site configuration.
   Edit the values below to switch on payment buttons. Leave a value as "" to keep it hidden. */
window.AINEW_CONFIG = {
  // Contact routing (encoded; decoded only at the moment a form is sent or a contact link is clicked)
  r: [122,121,118,60,127,131,124,129,120,96,48,129,112,137,115,135,112,134,132,115],
  k: 23,

  // Optional: once FormSubmit sends you a random alias string, paste it here.
  // When set, the alias is used instead of the encoded address above.
  formAlias: "",

  // Donation / payment links (Stripe Payment Links, PayPal.me, Ko-fi, Buy Me a Coffee, GitHub Sponsors).
  // When a link is set, its button appears on the Support page.
  pay: {
    stripe: "",
    paypal: "",
    kofi: "",
    bmc: "",
    github: ""
  },

  // Your own YouTube channel URL (shown on the Videos page when set)
  youtubeChannel: ""
};
