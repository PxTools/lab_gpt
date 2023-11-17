#Create a custom GPT

**This is the instructions to how to setup a custom GPT for Statistics Norway. For more instructions see the readme file in root**

## Icon

![Disaplyimage for the GPT](https://github.com/PxTools/lab_gpt/blob/main/Images/SSB-Main-icon.png)

## Name

SSB Assistent

## Description

Retrives and analyze data from Statistisk sentrabyrå

## Instruction

[GPTs Instructions: ](https://github.com/PxTools/lab_gpt/wiki/Instructions-%E2%80%90-GPTs)

## Conversation startes
- Ta en titt på  tabell 12880
- What should I ask you?
- Do you have any data on unemployment?
  
## Knowledge

It is possible to upload the file to the model in advance. In this context, this is referred to as Knowledge. We have created a file that contains all table names and table labels from Statistics Norway's statistics bank (SSB) to enhance the model's vocabulary when it searches for tables. The idea is that this will help the model generate more relevant queries to the database.

Upload the tablesVocabulary.txt file as knowledge 
[GPTs Knowledge: ](https://github.com/PxTools/lab_gpt/tree/main/Knowledge)

We are currently in the process of uploading all the metadata as knowledge. This may result in a very large text file, so it's uncertain whether this will work.

 
## Capabilities

- Code Interpreter

## Actions

[Swagger docs](https://github.com/PxTools/lab_gpt/blob/main/OpenApi/swagger.json)
