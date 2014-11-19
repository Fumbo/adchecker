$('#help').click(function () {
    var intro = introJs();

    intro.setOptions({
        steps: [
            {
                element: '#nav',
                intro: '<p class="h4 text-uc"><strong>1: Menu</strong></p><p>Naviguer en utilisant le menu.</p>',
                position: 'right'
            },
            {
                element: '#profile',
                intro: '<p class="h4 text-uc"><strong>2: Votre profile</strong></p><p>Gerez votre profile</p>',
                position: 'left'
            },
            {
                element: '#voscampagnes',
                intro: '<p class="h4 text-uc"><strong>3: La liste de vos campagnes</strong></p><p>C\'est ici que vous voulez retrouvez les informations relatives a vos campagnes et ainsi y acceder.</p>',
                position: 'bottom'
            },
        ],
        showBullets: true
    });
    intro.start()
});
