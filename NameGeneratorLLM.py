# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:19:25 2024

@author: Swati
"""

from secretKey import *
import os
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

os.environ["HUGGINGFACEHUB_API_TOKEN"] = hugging_face_token

llm = HuggingFaceHub(
    repo_id="huggingfaceh4/zephyr-7b-alpha", 
    model_kwargs={"temperature": 0.6, "max_length": 64,"max_new_tokens":512}
)


def GenerateBabyNames(gender:str, nationality:str) -> list[str]:
    
    ### create template string to be fed to LLMs with place holders
    prompt_template = PromptTemplate(
            input_variables = ['gender', 'nationality'],
            template = """I want to find a name for a {nationality} {gender}
                        baby. Suggest top 5 popular names for the baby. 
                        Return it as a comma separated list"""
        )
    
    
    ### For formatting the input prompt with the actual values in the 
    ### placeholders and feeds it to the LLMs
    llm_chain = LLMChain(llm = llm,
                         prompt = prompt_template,
                         output_key = 'baby_names'
        )

    ### Handling multiple inputs and outputs    
    chain = SequentialChain(
                chains = [llm_chain],
                input_variables = ['gender', 'nationality'],
                output_variables = ['baby_names']
        
        )
    
    response = chain({'gender':gender, 'nationality':nationality})
    
    return response
    
    