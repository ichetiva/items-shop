const currencySelector = document.getElementById('prices')

const getStripeSession = (itemId) => {
    let currency = currencySelector.selectedOptions[0].value;
    fetch(`/buy/${itemId}/${currency}`)
    .then(res => { return res.json() })
    .then(data => {
        const stripe = Stripe('pk_test_51MdbXKKZeqQ1jsp0rXsHKsHNZ7JU21xxOfMdvg51tXMSJ8BLf8mYUA7Og8EBGpZ4Pmao2jZ3qeNjTZHpQ8RF0gBL00Kdj2Jb66')
        stripe.redirectToCheckout({ sessionId: data['session_id']})
    })
}
