# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt  # Disable CSRF protection for simplicity in this example
def receive_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # Process the data as needed
            # ...
            print("this worked")

            return JsonResponse({"message": "Data received successfully"})
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
