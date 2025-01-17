prompts = {"default": "Remind me to select the proper text analysis task!",
"list_gen": """Instructions
---
Create a list of 10 article headlines for the topic: digital marketing.

Example output
---
- 10 Digital Marketing Strategies
- That Will Boost Your Business Growth
- 5 Dos and 10 Don'ts
- How to Use Influencer Marketing to Reach Your Target Audience

Rules
---
Don't talk about SEO in the article titles
Also avoid including any references to blogging, or email marketing with the generated headlines:
---""",
"sentiment_analysis": """You are working as a data analyst for a company that wants to improve customer satisfaction. Your task is to perform sentiment analysis on customer reviews of their product.

The label must be neutral, negative or positive
---
product review text: This marketing product was a complete waste of time and money. It didn't do anything it promised and the customer service was terrible. I'm very unhappy with the purchase and would not recommend it to anyone.
sentiment: negative
product review text: I recently purchased a marketing product from this company and I am so glad I did. The product was exactly what I was looking for, and the customer service was outstanding. The staff was very helpful and knowledgeable and they made sure I got exactly what I needed. I highly recommend this company and their products.
sentiment: positive
product review text: 
This product is an effective marketing tool that is easy to use. It has a lot of features that can help with creating a successful marketing campaign. However, it does have some drawbacks that should be taken into consideration when deciding if it is the right solution for your needs. Overall, the product is worth considering.
sentiment: neutral
---
product review text:  I recently purchased a marketing product from this company and I am so pleased with the results. The product is easy to use and the customer service team was incredibly helpful. They provided me with clear instructions and answered all my questions. The product has already improved my marketing efforts, and I look forward to seeing even better results in the future.
sentiment:
""",
"explain_liam5": """Explain the text below like I’m five:
Impossibility theorem, in political science, the thesis that it is generally impossible to assess the common good. It was first formulated in Social Choice and Individual Values (1951) by Kenneth J. Arrow, who was awarded (with Sir John R. Hicks) the Nobel Prize for Economics in 1972 partially in recognition of his work on the theorem. As a central element of rational choice theory, which attempts to explain political behavior as the rational pursuit of individual self-interest, the impossibility theorem posed a major challenge to 20th-century welfare economics and to a reevaluation of how democratic decision procedures arrive at representative expressions of individuals’ preferences. It has also been used to challenge the concept of “the public” as a meaningful social entity.
The impossibility theorem assumes that agents have complete and well-ordered preferences over all the outcomes under consideration in a collective choice situation. This requires that agents know whether they prefer one in any pair of possible outcomes, and it requires that agents’ preferences obey the logical relationship of transitivity, which requires that if Adams is preferred to Madison and Madison is preferred to Washington, then Washington cannot be preferred to Adams. The impossibility theorem considers cases in which three or more agents make a collective choice from three or more alternatives in situations as diverse as democratic voting, establishing public policies that reflect social welfare, and the marketplace. The theorem is constructed to resolve the question of whether there is any mathematical procedure for amalgamating individual preferences that results in a collectively rational preference ordering of all the possible outcomes.
In addition to assuming that individuals’ preferences are rational, the theorem stipulates that four minimal conditions must apply to the decision procedure for its result to be valid. The theorem requires that individuals be permitted to have any rational preference ordering over alternatives, that there not be a single dictator whose preference over a single pair of alternatives holds for the group decision, that the collective ranking over outcomes remains unchanged if one of the alternatives ceases to be considered, and that a unanimous preference over a pair of outcomes implies a collective preference over that pair. These requirements are generally regarded as beyond controversy.
The theorem proves that, given these minimal assumptions, it is impossible to construct any procedure that results in a collectively rational expression of individual desires. Though highly technical in its statement, the theorem has important implications for philosophies of democracy and political economy. The theorem rejects the notion of a collective democratic will, whether derived through civic deliberation or construed by experts who paternalistically apply knowledge of what is best for a population. The theorem also denies that there could be objective basic needs or universal criteria that any procedure for collective decision making should recognize, such as minimal nutrition standards or human rights.
""",
"least_to_most":"""
# Create a list of 3 Disney characters.
## For each character, generate a short biography to tell me more about the character.
""",
"step_by_step": """
# Follow these steps:
## Step 1: 
Condense the text enclosed in triple quotes into a single sentence.

## Step 2: 
Translate the summarized text into {0}.

# Output format
Summary: <output from Step 1>.
{0} Translation: <output from Step 2>

'''{1}'''
""",
"step_by_step_1":"""
Step 1 - The user will hand over a chunk of text enclosed in triple 
quotes. Your task is to condense this text into a single sentence, 
starting with the phrase "Summary: ".

Step 2 - Translate the summarization you made in Step 1 into {0}, 
leading the translation with the phrase "Translation: "

'''{1}'''
"""

}

def fetch_prompt(prompt_key="default", params=None):
    """
    Fetch a prompt by key and format it with optional parameters.

    Args:
        prompt_key (str, optional): The key of the prompt. Defaults to "default".
        params (list, optional): A list of parameters to format the prompt. Defaults to None.

    Returns:
        str: The formatted prompt.

    Raises:
        TypeError: If params is not a list.
    """
    prompt = prompts.get(prompt_key, "default")
    if params is not None:
        if not isinstance(params, list):
            raise TypeError("params must be a list")
        prompt = prompt.format(*params)
    return prompt

if __name__ == "__main__":
    print(fetch_prompt("step_by_step", ['Spanish','HAPPY DATA']))