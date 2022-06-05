

/*===================================================================================*/
/*	CUSTOM JS/JQUERY SCRIPTS
/*===================================================================================*/

// Insert your own scripts in here!
$('li.searchbox a').on('click', function (event) {
    $(this).parent().toggleClass('open');
});

$('body').on('click', function (e) {
    if (!$('li.searchbox').is(e.target) 
        && $('li.searchbox').has(e.target).length === 0 
        && $('.open').has(e.target).length === 0
    ) {
        $('li.searchbox').removeClass('open');
    }
});
