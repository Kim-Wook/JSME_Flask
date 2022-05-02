from flask import Flask, url_for, jsonify, request
from flask import render_template
from flask_bootstrap import Bootstrap
import urllib
from rdkit import Chem
from rdkit.Chem import Descriptors
 
app  = Flask(__name__)
Bootstrap( app )
 
@app.route('/')
def top():
    return render_template("jsme_simple.html")
 
@app.route('/mol_calc/')
def mol_calc():
    return render_template("mol_calc.html")
 
@app.route('/mol_calc/<smiles>/')
def do_calc(smiles):
    smiles = urllib.parse.unquote_plus( smiles )
    mol = Chem.MolFromSmiles( smiles )
    molwt = round(Descriptors.MolWt( mol ),2)
    hawt = round(Descriptors.HeavyAtomMolWt( mol ),2)
    return jsonify( molwt = molwt, hawt = hawt )
 
if __name__ =="__main__":
    app.run(debug = True)