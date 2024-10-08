from flask import render_template, url_for, flash, redirect, request
from app import app, get_db
from forms import MarketForm, InterventionForm, InvoiceForm

@app.route('/')
def home():
    return render_template('index.html')

# Routes for Market
@app.route('/market', methods=['GET'])
def market_list():
    db = get_db()
    markets = db.execute('SELECT * FROM market').fetchall()
    return render_template('market_list.html', markets=markets)

@app.route('/market/new', methods=['GET', 'POST'])
def new_market():
    form = MarketForm()
    if form.validate_on_submit():
        db = get_db()
        db.execute('INSERT INTO market (name, description) VALUES (?, ?)', 
                   (form.name.data, form.description.data))
        db.commit()
        flash('Market has been created!', 'success')
        return redirect(url_for('market_list'))
    return render_template('market_form.html', form=form)

@app.route('/market/edit/<int:id>', methods=['GET', 'POST'])
def edit_market(id):
    db = get_db()
    market = db.execute('SELECT * FROM market WHERE id = ?', (id,)).fetchone()
    form = MarketForm(obj=market)
    if form.validate_on_submit():
        db.execute('UPDATE market SET name = ?, description = ? WHERE id = ?',
                   (form.name.data, form.description.data, id))
        db.commit()
        flash('Market has been updated!', 'success')
        return redirect(url_for('market_list'))
    return render_template('market_form.html', form=form)

@app.route('/market/delete/<int:id>')
def delete_market(id):
    db = get_db()
    db.execute('DELETE FROM market WHERE id = ?', (id,))
    db.commit()
    flash('Market has been deleted!', 'success')
    return redirect(url_for('market_list'))

# Routes for Intervention
@app.route('/intervention', methods=['GET'])
def intervention_list():
    db = get_db()
    interventions = db.execute('SELECT * FROM intervention').fetchall()
    return render_template('intervention_list.html', interventions=interventions)

@app.route('/intervention/new', methods=['GET', 'POST'])
def new_intervention():
    form = InterventionForm()
    if form.validate_on_submit():
        db = get_db()
        db.execute('INSERT INTO intervention (date, provider, is_valid, market_id) VALUES (?, ?, ?, ?)',
                   (form.date.data, form.provider.data, form.is_valid.data, form.market_id.data))
        db.commit()
        flash('Intervention has been created!', 'success')
        return redirect(url_for('intervention_list'))
    return render_template('intervention_form.html', form=form)

@app.route('/intervention/edit/<int:id>', methods=['GET', 'POST'])
def edit_intervention(id):
    db = get_db()
    intervention = db.execute('SELECT * FROM intervention WHERE id = ?', (id,)).fetchone()
    form = InterventionForm(obj=intervention)
    if form.validate_on_submit():
        db.execute('UPDATE intervention SET date = ?, provider = ?, is_valid = ?, market_id = ? WHERE id = ?',
                   (form.date.data, form.provider.data, form.is_valid.data, form.market_id.data, id))
        db.commit()
        flash('Intervention has been updated!', 'success')
        return redirect(url_for('intervention_list'))
    return render_template('intervention_form.html', form=form)

@app.route('/intervention/delete/<int:id>')
def delete_intervention(id):
    db = get_db()
    db.execute('DELETE FROM intervention WHERE id = ?', (id,))
    db.commit()
    flash('Intervention has been deleted!', 'success')
    return redirect(url_for('intervention_list'))

# Routes for Invoice
@app.route('/invoice', methods=['GET'])
def invoice_list():
    db = get_db()
    invoices = db.execute('SELECT * FROM invoice').fetchall()
    return render_template('invoice_list.html', invoices=invoices)

@app.route('/invoice/new', methods=['GET', 'POST'])
def new_invoice():
    form = InvoiceForm()
    if form.validate_on_submit():
        db = get_db()
        db.execute('INSERT INTO invoice (amount, price, intervention_id) VALUES (?, ?, ?)',
                   (form.amount.data, form.price.data, form.intervention_id.data))
        db.commit()
        flash('Invoice has been created!', 'success')
        return redirect(url_for('invoice_list'))
    return render_template('invoice_form.html', form=form)

@app.route('/invoice/edit/<int:id>', methods=['GET', 'POST'])
def edit_invoice(id):
    db = get_db()
    invoice = db.execute('SELECT * FROM invoice WHERE id = ?', (id,)).fetchone()
    form = InvoiceForm(obj=invoice)
    if form.validate_on_submit():
        db.execute('UPDATE invoice SET amount = ?, price = ?, intervention_id = ? WHERE id = ?',
                   (form.amount.data, form.price.data, form.intervention_id.data, id))
        db.commit()
        flash('Invoice has been updated!', 'success')
        return redirect(url_for('invoice_list'))
    return render_template('invoice_form.html', form=form)

@app.route('/invoice/delete/<int:id>')
def delete_invoice(id):
    db = get_db()
    db.execute('DELETE FROM invoice WHERE id = ?', (id,))
    db.commit()
    flash('Invoice has been deleted!', 'success')
    return redirect(url_for('invoice_list'))
