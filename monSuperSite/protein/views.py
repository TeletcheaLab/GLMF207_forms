# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from protein.models import Protein
from protein.forms import proteinForm

# Create your views here.
def one_protein(request, identifiant):
    my_dict={}

    my_protein=get_object_or_404(Protein, pk=identifiant)
    my_dict['protein']=my_protein

    my_ligands=my_protein.ligand_set.all()
    my_dict['ligands']=my_ligands

    my_molecules=my_protein.molecule_set.all()
    my_dict['molecules']=my_molecules
    return render(request,"one_protein.html",my_dict)

def add(request):
	f = proteinForm
	return render(request, "add.html", {'f':f})

def add_boostrap(request):
	f = proteinForm
	return render(request, "add_boostrap.html", {'f':f})
