var updateButtons = document.getElementsByClassName('update-shopping-cart')

for (i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

        console.log('User:', user)
        if (user == 'AnonymousUser'){
            console.log('User not signed in')
        }else{
            console.log('Sign in successfull, granting access...')
        }
    })
}