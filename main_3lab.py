import flask
app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculate_mortgage():
    if request.method == 'POST':
        num_1 = request.form.get('num_1')
        num_2 = request.form.get('num_2')
        try:
            principal = float(num_1)  # Сумма кредита
            interest_rate = float(num_2) / 100  # Процентная ставка (в долях)
            num_payments = 30 * 12  # Срок кредита в месяцах (например, 30 лет)

            monthly_interest_rate = interest_rate / 12
            monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

            return render_template('result.html', ans=monthly_payment)
        except ValueError:
            return "Invalid input. Please enter valid numbers."
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
