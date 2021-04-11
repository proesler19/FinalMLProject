
def predict_cancellation(choice):
    if choice[0]:
        return 'User will probably cancel the booking.'
    else:
        return 'User will continue the booking.'