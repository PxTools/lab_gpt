# 🤖 SSB GPT - Setup Guide

```
💡 You need a ChatGPT 4 Subscription before you start
```

This document explains how to setup your own custom GPT for Statistics Norway (SSB).

If you don't want to set it up yourself and customize it, you can use the live version below:

- **Public GPT** - [SSB Assistent (beta)](https://chat.openai.com/g/g-JWtp8Chv5-ssb-assistent-beta)

## 📋 Setup

1. Head over to [ChatGPT's Website](https://chat.openai.com).
2. Click "**Explore**" in the sidebar.
3. Click "**Create GPT**" to start creating your GPT.
4. Click "**Configure**" to customize your GPT.

### GPT Information `(Optional)`

1. **Logo:** Download one of the SSB logos below, or use your own image.

   <a href="./images/logo_dark.png"><img src="./images/logo_dark.png" width=60 height=60 ></a>
   <a href="./images/logo_white.png"><img src="./images/logo_white.png" width=60 height=60 ></a>

2. **Logo:** Click "**+**" button to set GPT logo.
3. **Name:** Set your GPT's name to the example below, or give it your own custom name.

   `Example:` _SSB Assistant_

4. **Description:** Set your GPT's description to the example below, or give it your own custom description.

   `Example:` _A GPT-powered tool for extracting, analyzing, and visualizing data from Statistics Norway. Ideal for research, policy analysis, and education._

5. **Conversation starters:** Set your GPT's example prompts from the examples below, or add your own custom examples.

   `Examples:`

   - _Ta en titt på tabell 12880_
   - _What should I ask you?_
   - _Do you have any data on unemployment?_
   - _Hey, could you please find main economic indicators for housing prices from 2023 to 2026 in terms of percentage change?_

### GPT Data `(Required)`

```
💡 There are two versions to chose from:
    - V0: is what SSB is using, and has more updated data.
    - V2: provides better results, but has less data available.
```

1. **Instructions:** Copy and paste one of the instructions below into your GPT's instructions.
   - [Instructions V0](./instructions/instructions_v0.txt)
   - [Instructions V2](./instructions/instructions_v2.txt)
2. **Knowledge:** Download and upload the knowledge files listed below.
   - [vocabulary_english.txt](./knowledge/vocabulary_english.txt)
   - [vocabulary_norwegian.txt](./knowledge/vocabulary_norwegian.txt)
   - [api_documentation.pdf](./knowledge/api_documentation.pdf)
   - [graph_background.png](./knowledge/graph_background.png)
3. **Capabilities:** Only select _Code interpreter_ for your GPT's capabilities.
4. **Actions:** Click _Create new action_ button and copy paste both files listed below in separate actions. Select either V0 or V2 depending on the instructions you previously opted for.
   - [Action (Time)](./actions/swagger_time.json)
   - [Action (V0)](./actions/swagger_v0.json) - Add if using V0 instructions
   - [Action (V2)](./actions/swagger_v2.json) - Add if using V2 instructions

### GPT Usage

You can now use your own SSB Assistant GPT!

- You can use the GPT in preview mode (available while editing the GPT). This will display all the requests and responses the GPT gets while interacting with the Actions/API Docs you added. This is a nice way to debug and understand where the GPT makes mistakes.
- You can also use your GPT in your ChatGPT interface if you save the GPT for "only me", "people with link" or "public".
