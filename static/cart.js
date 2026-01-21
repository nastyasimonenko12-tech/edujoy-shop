document.addEventListener('DOMContentLoaded', function() {
    function updateCartCount(count) {
        document.querySelectorAll('#cart-count').forEach(el => el.textContent = count);
    }

    document.querySelectorAll('.cart-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const id = this.dataset.id;
            fetch('/add', {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'}, body:'id='+id})
                .then(resp => resp.json())
                .then(count => updateCartCount(count));
        });
    });

    document.querySelectorAll('.plus-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const id = this.dataset.id;
            fetch('/add', {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'}, body:'id='+id})
                .then(resp => resp.json())
                .then(count => updateCartCount(count))
                .then(()=> location.reload());
        });
    });

    document.querySelectorAll('.minus-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const id = this.dataset.id;
            fetch('/minus', {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'}, body:'id='+id})
                .then(resp => resp.json())
                .then(count => updateCartCount(count))
                .then(()=> location.reload());
        });
    });

    const clearBtn = document.querySelector('.clear-btn');
    if(clearBtn){
        clearBtn.addEventListener('click', function(){
            fetch('/clear', {method:'POST'})
            .then(resp => resp.json())
            .then(count => {
                updateCartCount(count);
                location.reload();
            });
        });
    }
});