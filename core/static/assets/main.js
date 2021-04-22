
$(document).ready(function () {
    var score = document.getElementById('score')
    const star1 = document.getElementById('star1')
    const star2 = document.getElementById('star2')
    const star3 = document.getElementById('star3')
    const star4 = document.getElementById('star4')
    const star5 = document.getElementById('star5')
    console.log(star1)
    const arr = [star1, star2, star3, star4, star5]

    if (score != null) {
        score = score.value
        switch (score) {
            case '1': {
                star1.classList.add('checked')
                star2.classList.remove('checked')
                star3.classList.remove('checked')
                star4.classList.remove('checked')
                star5.classList.remove('checked')
                return
            }
            case '2': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.remove('checked')
                star4.classList.remove('checked')
                star5.classList.remove('checked')
                return
            }
            case '3': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.add('checked')
                star4.classList.remove('checked')
                star5.classList.remove('checked')
                return
            }
            case '4': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.add('checked')
                star4.classList.add('checked')
                star5.classList.remove('checked')
                return
            }
            case '5': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.add('checked')
                star4.classList.add('checked')
                star5.classList.add('checked')
                return
            }
        }
    }
    const hadleSelect = (selection) => {
        console.log('entrou aqui')
        switch (selection) {
            case 'star1': {
                star1.classList.add('checked')
                star2.classList.remove('checked')
                star3.classList.remove('checked')
                star4.classList.remove('checked')
                star5.classList.remove('checked')
                return
            }
            case 'star2': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.remove('checked')
                star4.classList.remove('checked')
                star5.classList.remove('checked')
                return
            }
            case 'star3': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.add('checked')
                star4.classList.remove('checked')
                star5.classList.remove('checked')
                return
            }
            case 'star4': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.add('checked')
                star4.classList.add('checked')
                star5.classList.remove('checked')
                return
            }
            case 'star5': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.add('checked')
                star4.classList.add('checked')
                star5.classList.add('checked')
                return
            }
        }
    }
    console.log('dsdas', typeof (arr))
    arr.forEach(item => item.addEventListener('mouseover', (event) => {
        console.log('entrou no for')
        console.log(event.target)
    }))
});



function carregaStar(score) {
    const star1 = document.getElementById('star1')
    const star2 = document.getElementById('star2')
    const star3 = document.getElementById('star3')
    const star4 = document.getElementById('star4')
    const star5 = document.getElementById('star5')

    console.log(star2)
    const arr = [star1, star2, star3, star4, star5]
    console.log(arr)
    const hadleSelect = (score) => {
        switch (score) {
            case 'star1': {
                star1.classList.add('checked')
                star2.classList.remove('checked')
                star3.classList.remove('checked')
                star4.classList.remove('checked')
                star5.classList.remove('checked')
                return
            }
            case 'star2': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.remove('checked')
                star4.classList.remove('checked')
                star5.classList.remove('checked')
                return
            }
            case 'star3': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.add('checked')
                star4.classList.remove('checked')
                star5.classList.remove('checked')
                return
            }
            case 'star4': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.add('checked')
                star4.classList.add('checked')
                star5.classList.remove('checked')
                return
            }
            case 'star5': {
                star1.classList.add('checked')
                star2.classList.add('checked')
                star3.classList.add('checked')
                star4.classList.add('checked')
                star5.classList.add('checked')
                return
            }
        }
    }

    arr.forEach(item => item.addEventListener('mouseover', (event) => {
        console.log(event.target)
    }))
}
