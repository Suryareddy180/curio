import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings

# Configure Gemini
genai.configure(api_key='AIzaSyBcSbsPyUgH_7B7ZraCugyGEgUt1dLTJVs')

def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        if user_input:
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content(user_input)
            bot_response = response.text
        else:
            bot_response = "Please enter a valid question."
        
        return render(request, 'chat/chat.html', {
            'user_input': user_input,
            'bot_response': bot_response,
        })

    return render(request, 'chat/chat.html')
