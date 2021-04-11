# FinalMLProject

Input Template:

Example of not likely cancellation: 

http://0.0.0.0:8080/engr-222/predict_cancellation/1/2/0/0/0/0/0/2
{
  "accuracy": "75%", 
  "prediction": "Will not likely cancel"
}


Example of likely cancellation:

http://0.0.0.0:8080/engr-222/predict_cancellation/1/2/1/2/0/3/2/2
{
  "accuracy": "75%", 
  "prediction": "Will likely cancel"
}



{'City Hotel': 0, 'Resort Hotel': 1}
{'Aviation': 0, 'Complementary': 1, 'Corporate': 2, 'Direct': 3, 'Groups': 4, 'Offline TA/TO': 5, 'Online TA': 6, 'Undefined': 7}
{'No Deposit': 0, 'Non Refund': 1, 'Refundable': 2}
{'Month of Booking': 'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9, 'October' : 10, 'November' : 11, 'December' : 12}
{'Arrival Date': '0 - infinity'}
{'Week Nights': '0 - infinity'}
{'Weekend Nights': '0 - infinity'}
{'Adults': '0 - infinity'}


[ Hotel Type(0-1), Market Segment(0-7), Deposit Type(0-1), 
Month of Booking(0-12), Day(0-31), Weeknights(0-inf), 
Weekend Nights(0-inf), Adults(0-inf) ]
