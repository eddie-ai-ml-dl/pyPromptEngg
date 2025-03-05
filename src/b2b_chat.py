from src.geminiChatBot import GeminiChatbot
import time
import random


def bot_to_bot_chat(bot1_initial_prompt, bot2_initial_prompt, max_iterations=20, max_retries=3):
    bot1=GeminiChatbot(model_name="models/gemini-2.0-flash-exp")
    bot2=GeminiChatbot(model_name="models/gemini-1.5-flash", system_instruction=bot2_initial_prompt)

    def delay_response(bot, prompt, max_retries=max_retries):
        retries=0
        response=bot.send_message(prompt)
        while retries<max_retries and response.lower()[:10]=="**error:**":
            seconds=round(random.uniform(1, 2), 2)
            print(f"Delaying for {seconds} seconds...")
            retries+=1
            time.sleep(seconds)
            response=bot.send_message(prompt)
        return response

    print('#'*25, "START: B2B CONVERSATION", "#"*25)

    i=0
    b1_response=bot1.send_message(bot1_initial_prompt)
    while i<max_iterations:
        i+=1
        print(f"TUTOR ({bot1.model_name}) /???> {b1_response}")

        b2_response=delay_response(bot2, b1_response)
        print(f"STUDENT ({bot2.model_name}) /~~~> {b2_response}")

        if "bye" in b1_response.lower():
            print("#"*25, "END: B2B CONVERSATION", "#"*25)
            break

        b1_response=delay_response(bot1, b2_response)