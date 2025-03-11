from transformers import AutoModelForCausalLM, AutoTokenizer
import pandas as pd
import json


def analyze_and_answer(question, context_str, think=True):  
    question = question.lower()
    prompt = "Please reason step by step, put your final answer within 20 words and start the final answer in words: 'the final answer is:'."
    
    if think:
        user_prompt = context_str + question + prompt + "\n<think>\n"
    else:
        user_prompt = context_str + question + prompt
        
    inputs = tokenizer(user_prompt, return_tensors="pt")
    # Generate with recommended temperature of 0.6
    outputs = model.generate(**inputs,
        max_new_tokens=2000,
        temperature=0.1,  # Recommended temperature
        pad_token_id=tokenizer.eos_token_id)
    
    # Decode the output
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=False)
    
    return generated_text

# in this specific case (small tabular data and SML model) due to the attention mechanism the model gives more accurate result if the tabular data covert to text with context.  
def excel_to_narrative_oneline(data_path): 
    df = pd.read_excel(data_path, sheet_name="Sheet1")
    
    # Group by company name
    grouped_by_company = df.groupby('company name')
    
    # Generate narrative for each company
    company_narratives = []
    
    for company_name, group in grouped_by_company:
        tool_descriptions = []
        
        for _, row in group.iterrows():
            tool_desc = (f"company {company_name} have {row['tool number per each company']} {row['tool name']} tools with {row['labor hours per tool']} labor per each, and {row['material cost per tool']} per each")
            tool_descriptions.append(tool_desc)
        
        company_narratives.extend(tool_descriptions)
    
    # Join all tool descriptions into a single line with semicolons
    return "; ".join(company_narratives)




## and the code is:

# model_path = {the path to the model directory}
# data_path = {your path to the excel file

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

narrative = excel_to_narrative_oneline(data_path)

'''
# execution with chat bot:
def main():
    
    # Interactive query loop (for testing)
    while True:
        question = input("\nEnter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        
        # the thinking process take more time but produce more accurate answers
        answer = analyze_and_answer(question, narrative, think=True)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()'''


# simpler execution
questions = [
    "What is the total material (material * tool number) for TechCore?"
]
answer = analyze_and_answer(question, narrative, think=True)
print(f"Q: {question}")
print(f"A: {answer}")
