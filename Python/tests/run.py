# from recognizers_number.number.number_recognizer import recognize_number
from recognizers_date_time.date_time.date_time_recognizer import recognize_datetime

input_text = "6th of the 12th 1997"
# input_text = "6th of December"
# input_text = "Thursday the 6th"
# input_text = "On the tenth"
# input_text = "4th of the 3rd"
culture = "en-us"
results = recognize_datetime(input_text, culture)

if not results:
    print("No Results")
for result in results:
    print(result)
    for value in result.resolution.get("values"):
        print(value)

