from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    RedirectView, TemplateView, ListView, DetailView)
from .models import CartItem, Order
from accounts.models import User
from catalog.models import Product, Rating
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django import forms


class CreateCartItemView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product)
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso!')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso!')
        return reverse('checkout:cart_item')


class CartItemView(TemplateView):
    template_name = 'checkout/cart.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItem, fields=('quantity',), can_delete=True, extra=0
        )
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key and CartItem.objects.filter(cart_key=session_key).exists():
            cart_items = CartItem.objects.filter(cart_key=session_key)
            order = Order.objects.create_order(
                user=request.user, cart_items=cart_items
            )
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('checkout:cart_item')
        response = super(CheckoutView, self).get(request, *args, **kwargs)
        response.context_data['order'] = order
        return response


class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'checkout/order_list.html'
    paginate_by = 3

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = 'checkout/order_detail.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here !',
            'rows': 4,
            'cols': 50
        }))

    class Meta:
        model = Rating
        fields = ['content']


def ProductRatingView(request, *args, **kwargs):
    product = get_object_or_404(Product, slug=kwargs['slug'])
    template_name = 'checkout/avaliar_produto.html'
    ratings = Rating.objects.filter(product=product)
    new_rating = None
    cf = None
    done = False
    score_by_user = Rating.objects.filter(product=product).filter(user=request.user)

    if score_by_user:
        done = True
    else:
        new_rating = None
        if request.method == 'POST':
            cf = CommentForm(data=request.POST)
            if cf.is_valid():
                stored_ratings = Rating.objects.filter(product=product)
                score_sum = 0.0
                ratings_amount = len(stored_ratings)
                current_rating = float(request.POST.get('current-score'))

                for stored_rating in stored_ratings:
                    score_sum += float(stored_rating.score)

                score_sum += current_rating
                ratings_amount += 1

                content = request.POST.get('content')
                new_rating = cf.save(commit=False)
                new_rating.product = product
                new_rating.user = request.user
                new_rating.score = current_rating
                new_rating.comment = content
                new_rating.save()

                # update current product score
                product.score = score_sum / ratings_amount
                product.save()
        else:
            cf = CommentForm()
    return render(
        request,
        template_name,
        {
            'product': product,
            'comments': ratings,
            'new_rating': new_rating,
            'comment_form': cf,
            'done': done,
            'score_by_user': score_by_user[0].score if score_by_user else None
        }
    )

    """content = request.POST.get('content')
            comment = Rating.objects.create(
                user=request.user, product=product, score=self.kwargs['score'], comment=content)
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            cf = CommentForm()

    response = super(ProductRatingView, self).get(request, *args, **kwargs)
    response.context_data['product'] = product
    response.context_data['comment_form'] = cf
    return response
"""


def rating(request):
    if request.method == 'POST':
        rating = request.POST.get('content')

    date = datetime.now()
    user = None

    def get_queryset(self):
        user = User.objects.filter(user=self.request.user)


class PagSeguroView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        order_pk = self.kwargs.get('pk')
        order = get_object_or_404(
            Order.objects.filter(user=self.request.user), pk=order_pk
        )
        pg = order.pagseguro()
        pg.redirect_url = self.request.build_absolute_uri(
            reverse('checkout:order_detail', args=[order.pk])
        )

        response = pg.checkout()
        return response.payment_url


create_cartitem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()
checkout = CheckoutView.as_view()
order_list = OrderListView.as_view()
order_detail = OrderDetailView.as_view()
rating_product = ProductRatingView
pagseguro_view = PagSeguroView.as_view()
