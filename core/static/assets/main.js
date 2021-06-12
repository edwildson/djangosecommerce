$(document).ready(function () {
    $('.rate-product span').on('click', handleStarClick);
});

function colourStarts(last_star_index) {
    let is_marked = false;

    for (let it = 0; it < 5; it++) {
        is_marked = $('.rate-product span')
            .eq(it)
            .hasClass('fa-star');

        $('.rate-product span').eq(it)
            .removeClass('fa-star')
            .removeClass('fa-star-o')
            .removeClass('fa-star-half-o');

        if (it <= last_star_index) {
            if (is_marked && it == last_star_index) {
                $('.rate-product span')
                    .eq(it)
                    .addClass('fa-star-half-o');
                continue;
            }

            $('.rate-product span')
                .eq(it)
                .addClass('fa-star');

            continue;
        }

        $('.rate-product span')
            .eq(it)
            .addClass('fa-star-o');
    }
}

function updateScore(last_star_index) {
    let current_score_tag = $('#current-score');
    let current_score = 0;

    for (let it = 0; it <= last_star_index; it++) {
        if ($('.rate-product span').eq(it).hasClass('fa-star')) {
            current_score += 1;
            continue;
        }
        current_score += 0.5;
    }

    current_score_tag.val(current_score);
}

function handleStarClick() {
    let clicked_start_index = $(this).index();
    colourStarts(clicked_start_index);
    updateScore(clicked_start_index);
}

