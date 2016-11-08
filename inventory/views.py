from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Tag, Item, Loan
from .forms import ItemForm, LoanForm, TagForm


# TODO tekst på knapper må midtstilles
# TODO knapper må flyttes til bestemt punkt på skjermen
# TODO lage søkeside
# TODO mulig å bruke QR-kode for merking av gjenstander, må føre til item sin detail-side

def index(request):
    items = Item.objects.all()
    # items.sort(key=lambda a: a.tags.get(pk=1))
    item_dict = {}  # TODO vurdere å bytte ut med en sorted dict for å kunne vise kategoriene sortert,
    # evt legge kategorier i en sortert liste
    no_category = []
    for item in items:
        if not item.tags.all():
            no_category.append(item)

        for tag in item.tags.all():
            try:
                item_dict[tag].append(item)
            except KeyError:
                item_dict[tag] = [item]

    for value in item_dict.values():
        value.sort(key=lambda e: e.name.title())

    context = {
        'item_dict': item_dict,
        'no_category': no_category,
    }
    return render(request, 'inventory/index.html', context)


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'inventory/detail.html', {'item': item})


# @login_required  # TODO tilgjenelighet må endres mtp om man er innlogget eller ikke
def add_item(request, item_id=0):
    message = "Legg til en ny gjenstand"
    button_message = "registrer"

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            if item_id != '0':  # existing item to be changed
                item = Item.objects.get(pk=item_id)
                item.name = form.cleaned_data['name']
                item.description = form.cleaned_data['description']
                item.quantity = form.cleaned_data['quantity']
                item.tags = form.cleaned_data['tags']
                item.save()
            else:  # create new item from form
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                quantity = form.cleaned_data['quantity']
                tags = form.cleaned_data['tags']
                item = Item(name=name, description=description, quantity=quantity)
                item.save()

            # TODO legge til at en liten melding vises øverst når man laster inn neste side, se: "the messages framwork"
            return HttpResponseRedirect(reverse('inventory:registered'))
    else:
        form = ItemForm()

        if item_id:
            message = "Endre gjenstand"
            button_message = "endre"

            item = Item.objects.get(pk=item_id)
            initial = {
                'name': item.name,
                'description': item.description,
                'quantity': item.quantity,
                'tags': item.tags,
            }
            form = ItemForm(initial=initial)

    context = {
        'form': form,
        'message': message,
        'button_message': button_message,
        'item_id': item_id,
    }
    return render(request, 'inventory/add_item.html', context)


# @login_required  # TODO tilgjenelighet må endres mtp om man er innlogget eller ikke
def add_tag(request, tag_id=0):
    message = "Legg til ny tag"
    button_message = "Legg til"

    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            if tag_id != '0':  # form sender streng tilbake, selv om den passes som inten 0 i context
                tag = Tag.objects.get(pk=tag_id)
                tag.name = form.cleaned_data['name']
                tag.save()
            else:
                name = form.cleaned_data['name']
                tag = Tag(name=name)
                tag.save()

            # TODO legge til at en liten melding vises øverst når man laster inn neste side, se: "the messages framwork"
            return HttpResponseRedirect(reverse('inventory:registered'))
    else:
        form = TagForm()
        if tag_id:
            message = "Endre tag"
            button_message = "Endre"
            tag = Tag.objects.get(pk=tag_id)
            form = TagForm(initial={'name': tag.name})

    context = {
        'form': form,
        'message': message,
        'button_message': button_message,
        'tag_id': tag_id,
    }
    return render(request, 'inventory/add_tag.html', context)


# @login_required  # TODO tilgjenelighet må endres mtp om man er innlogget eller ikke
def loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            borrower = form.cleaned_data['borrower']
            # TODO plukk ut bruker som var logget inn, og lagre i variabel lender
            comment = form.cleaned_data['comment']

            loan_date = timezone.now()
            return_date = form.cleaned_data['return_date']
            loan = Loan(item=item, borrower=borrower, comment=comment, loan_date=loan_date, return_date=return_date)
            loan.save()
            return HttpResponseRedirect(reverse('inventory:registered'))
    else:
        form = LoanForm()
    return HttpResponse(render(request, 'inventory/loan.html', {'form': form}))


def registered(request):
    name = "NAME"
    # TODO mulig å heller redirecte til index, og ha en toast som sier at item.name er registrert, må da finne en
    # måte å vise denne toasten selv om man kommer til ny side
    beskjed = '<p>Dette er en midlertidig side fra view registered, som bør erstattes med en toast</p>'

    return render(request, 'inventory/registered.html', {'type': name})


def tag_detail(request, tag_id):
    # TODO lage bedre oversikt over items, feks collapsible
    tag = get_object_or_404(Tag, pk=tag_id)
    related_items = tag.item_set.all()
    context = {
        'tag': tag,
        'related_items': related_items,
    }
    return render(request, 'inventory/tag_detail.html', context)
