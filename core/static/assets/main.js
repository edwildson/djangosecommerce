$(document).ready(function () {
    // var score = document.getElementById('score')
    // const star1 = document.getElementById('star1')
    // const star2 = document.getElementById('star2')
    // const star3 = document.getElementById('star3')
    // const star4 = document.getElementById('star4')
    // const star5 = document.getElementById('star5')
    // console.log(star1)
    // const arr = [star1, star2, star3, star4, star5]
    //
    // if (score != null) {
    //     score = score.value
    //     switch (score) {
    //         case '1': {
    //             star1.classList.add('checked')
    //             star2.classList.remove('checked')
    //             star3.classList.remove('checked')
    //             star4.classList.remove('checked')
    //             star5.classList.remove('checked')
    //             return
    //         }
    //         case '2': {
    //             star1.classList.add('checked')
    //             star2.classList.add('checked')
    //             star3.classList.remove('checked')
    //             star4.classList.remove('checked')
    //             star5.classList.remove('checked')
    //             return
    //         }
    //         case '3': {
    //             star1.classList.add('checked')
    //             star2.classList.add('checked')
    //             star3.classList.add('checked')
    //             star4.classList.remove('checked')
    //             star5.classList.remove('checked')
    //             return
    //         }
    //         case '4': {
    //             star1.classList.add('checked')
    //             star2.classList.add('checked')
    //             star3.classList.add('checked')
    //             star4.classList.add('checked')
    //             star5.classList.remove('checked')
    //             return
    //         }
    //         case '5': {
    //             star1.classList.add('checked')
    //             star2.classList.add('checked')
    //             star3.classList.add('checked')
    //             star4.classList.add('checked')
    //             star5.classList.add('checked')
    //             return
    //         }
    //     }
    // }
    // const hadleSelect = (selection) => {
    //     console.log('entrou aqui')
    //     switch (selection) {
    //         case 'star1': {
    //             star1.classList.add('checked')
    //             star2.classList.remove('checked')
    //             star3.classList.remove('checked')
    //             star4.classList.remove('checked')
    //             star5.classList.remove('checked')
    //             return
    //         }
    //         case 'star2': {
    //             star1.classList.add('checked')
    //             star2.classList.add('checked')
    //             star3.classList.remove('checked')
    //             star4.classList.remove('checked')
    //             star5.classList.remove('checked')
    //             return
    //         }
    //         case 'star3': {
    //             star1.classList.add('checked')
    //             star2.classList.add('checked')
    //             star3.classList.add('checked')
    //             star4.classList.remove('checked')
    //             star5.classList.remove('checked')
    //             return
    //         }
    //         case 'star4': {
    //             star1.classList.add('checked')
    //             star2.classList.add('checked')
    //             star3.classList.add('checked')
    //             star4.classList.add('checked')
    //             star5.classList.remove('checked')
    //             return
    //         }
    //         case 'star5': {
    //             star1.classList.add('checked')
    //             star2.classList.add('checked')
    //             star3.classList.add('checked')
    //             star4.classList.add('checked')
    //             star5.classList.add('checked')
    //             return
    //         }
    //     }
    // }
    // console.log('dsdas', typeof (arr))
    // arr.forEach(item => item.addEventListener('mouseover', (event) => {
    //     console.log('entrou no for')
    //     console.log(event.target)
    // }))


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


// function carregaStar(score) {
//     const star1 = document.getElementById('star1')
//     const star2 = document.getElementById('star2')
//     const star3 = document.getElementById('star3')
//     const star4 = document.getElementById('star4')
//     const star5 = document.getElementById('star5')
//
//     console.log(star2)
//     const arr = [star1, star2, star3, star4, star5]
//     console.log(arr)
//     const hadleSelect = (score) => {
//         switch (score) {
//             case 'star1': {
//                 star1.classList.add('checked')
//                 star2.classList.remove('checked')
//                 star3.classList.remove('checked')
//                 star4.classList.remove('checked')
//                 star5.classList.remove('checked')
//                 return
//             }
//             case 'star2': {
//                 star1.classList.add('checked')
//                 star2.classList.add('checked')
//                 star3.classList.remove('checked')
//                 star4.classList.remove('checked')
//                 star5.classList.remove('checked')
//                 return
//             }
//             case 'star3': {
//                 star1.classList.add('checked')
//                 star2.classList.add('checked')
//                 star3.classList.add('checked')
//                 star4.classList.remove('checked')
//                 star5.classList.remove('checked')
//                 return
//             }
//             case 'star4': {
//                 star1.classList.add('checked')
//                 star2.classList.add('checked')
//                 star3.classList.add('checked')
//                 star4.classList.add('checked')
//                 star5.classList.remove('checked')
//                 return
//             }
//             case 'star5': {
//                 star1.classList.add('checked')
//                 star2.classList.add('checked')
//                 star3.classList.add('checked')
//                 star4.classList.add('checked')
//                 star5.classList.add('checked')
//                 return
//             }
//         }
//     }
//
//     arr.forEach(item => item.addEventListener('mouseover', (event) => {
//         console.log(event.target)
//     }))
// }
