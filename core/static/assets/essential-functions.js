function createStars(product_index, product_score) {
    product_index = parseInt(product_index) - 1;

    let products_score_tag = document.getElementsByClassName('start-products')[product_index];

    product_score = parseFloat(product_score.replace(',', '.'));

    let product_score_int = parseInt(product_score);
    let product_score_mod = product_score % product_score_int;
    let new_element = null;

    if (product_score_mod)
        product_score = product_score_mod <= 0.5 ? (product_score_int + 0.5) : (product_score_int + 1);

    for (let it = 0; it < 5; it++) {
        new_element = document.createElement("span");
        new_element.classList.add("fa");

        if (product_score - it == 0.5)
            new_element.classList.add("fa-star-half-o");
        else if (it < product_score)
            new_element.classList.add("fa-star");
        else
            new_element.classList.add("fa-star-o");

        products_score_tag.append(new_element);
    }
}