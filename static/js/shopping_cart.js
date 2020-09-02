var updateButtons = document.getElementsByClassName('update-shopping-cart');


for (i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'Action:', action);
        console.log('USER:', user);
        if (user === 'AnonymousUser'){
            useCookies(productId, action);
        }else {
            updateUserOrder(productId, action);
        }
    });
}


function useCookies(productId, action) {
    console.log('User not signed in!')
    if (action == 'add') {
        if (shoppingCart[productId] === undefined) {
            shoppingCart[productId] = {'quantity':1}
        }
        else {
            shoppingCart[productId]['quantity'] += 1
        }
    }

    if (action == 'remove') {
        shoppingCart[productId]['quantity'] -= 1

        if (shoppingCart[productId]['quantity'] <= 0) {
            console.log('Remove item')
            delete shoppingCart[productId]
        }
    }

    document.cookie = 'shoppingCart=' + JSON.stringify(shoppingCart) + ";domain=;path=/"
    location.reload()
}


function updateUserOrder(productId, action){
    console.log('Sign in successfull, granting access...');
    var url = '/update_item/';
    console.log('URL:', url);

    fetch(url, {
        credentials: 'include',
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action}),
    })

    .then((response) => {
        return response.json();
    })

    .then((data) => {
        console.log('data:', data);
        location.reload();
    });
}