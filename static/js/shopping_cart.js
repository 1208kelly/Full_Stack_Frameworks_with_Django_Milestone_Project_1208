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
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('Sign in successfull, granting access...')
    var url = '/update_item/'
    console.log('URL:', url)

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) => {
        return response.json();
    })

    .then((data) => {
        location.reload()
    });
}