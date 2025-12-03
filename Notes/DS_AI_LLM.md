# 24.11.2025
## LLM
- [Тревога в мире LLM](https://telegra.ph/Trevoga-v-mire-LLM-11-10)
- COOL! [Defeating Nondeterminism in LLM Inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
- COOL! [On-Policy Distillation](https://thinkingmachines.ai/blog/on-policy-distillation/).
- [TOON](https://toonformat.dev/) Token-Oriented Object Notation
A compact, human-readable encoding of the JSON data model for LLM prompts.
- [Tokenization Experiment: Format Comparison](https://www.curiouslychase.com/playground/format-tokenization-exploration?mode=preset&size=small-simple&structure=uniform-flat)

# 23.10.2025
- [Cursor bug](https://forum.cursor.com/t/cursor-agent-mode-when-running-terminal-commands-often-hangs-up-the-terminal-requiring-a-click-to-pop-it-out-in-order-to-continue-commands/59969). Cursor agent mode - when running terminal commands often hangs up the terminal, requiring a click to pop it out in order to continue commands

# 07.10.2025
- [Giga-Embeddings](https://huggingface.co/ai-sage/Giga-Embeddings-instruct) топит всех на ruMTEB (http://mteb-leaderboard.hf.space/?benchmark_name=MTEB%28rus%2C+v1%29) с результатом 74.1 и при этом не жертвует качеством при работе с английским. Заточена под RAG-системы — даёт точный семантический поиск и не галлюцинирует. Это делает её идеальной для FAQ ботов и поиска по документации, но и для других задач, вроде дедупликации и кластеризации, она тоже подходит. А открытая лицензия и 3B параметров позволяют быстро интегрировать модель в прод.

# 30.09.2025
## LLM
- COOL! [LLM Context Management: How to Improve Performance and Lower Costs](https://eval.16x.engineer/blog/llm-context-management-guide)

# 23.09.2025
- [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://arxiv.org/pdf/2208.07339)
- [Quantization Deep Dive, или Введение в современную квантизацию](https://habr.com/ru/companies/yandex/articles/800945/)


# 18.09.2025
## LLM
- [How to Install LM Studio - A Graphical Application for Running Large Language Models (LLMs)](https://docs.vultr.com/how-to-install-lm-studio-a-graphical-application-for-running-large-language-models-llms)
- [How I Install LM Studio 0.3.2 on Ubuntu Studio 24.04 Linux](https://dimensionquest.net/2024/09/how-i-install-lm-studio-0.3.2-on-ubuntu-studio-24.04-linux/)
- [masgari/ollama-cli](https://github.com/masgari/ollama-cli. A simple CLI tool for interacting with multiple remote Ollama servers, no Ollama installation required)

## Claude
- [Claude Code Model Configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
- [Claude API Pricing Calculator](https://invertedstone.com/calculators/claude-pricing)
- [Models & pricing. Choosing the right model](https://docs.claude.com/en/docs/about-claude/models/choosing-a-model)
- [Models overivew](https://docs.claude.com/en/docs/about-claude/models/overview)

## Grok
- [Models and Pricing](https://docs.x.ai/docs/models)

# 17.09.2025
## Antropic API
- Временный USA WireGuard VPN. [Create Free VPN WireGuard USA 6](https://www.vpnjantit.com/create-free-account)
- [How to get your Anthropic API key (3 steps)](https://www.merge.dev/blog/anthropic-api-key)
	Step 1: Create an account. 
Sign up for an account [here](https://console.anthropic.com/login). Нынче это [Platform console](https://platform.claude.com/dashboard)
	Step 2: Generate an API Key 
After creating an account, click your Profile in the top right corner and select API Keys

- [How to get your Claude API key: A step-by-step guide](https://pickaxe.co/post/how-to-get-your-claude-api-key-a-step-by-step-guide)

# 15.09.2025
## LLM
- [Structured data extraction from unstructured content using LLM schemas](https://simonw.substack.com/p/structured-data-extraction-from-unstructured)
- [От слов к векторам: как эмбеддинги помогают моделям понимать нас - Блоги Epsilon Metrics] https://blogs.epsilonmetrics.ru/kak-embeddingi-pomogayut-llm-ponyat-nas/)
- [The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)

# 10.09.2025
## Vector database
- COOL [An Introduction to Vector Databases](https://qdrant.tech/articles/what-is-a-vector-database/). С диаграммами и схемами.
- Qdrant bulk upload
	- [Bulk Upload Vectors to a Qdrant Collection](https://qdrant.tech/documentation/database-tutorials/bulk-upload/)
	- [Uploading a large dataset to Qdrant - Data Loader slowing down](https://community.n8n.io/t/uploading-a-large-dataset-to-qdrant-data-loader-slowing-down/166481/2)

# 08.09.2025
## LLM
- [What makes Claude Code so damn good (and how to recreate that magic in your agent)!?](https://minusx.ai/blog/decoding-claude-code/)


# 11.08.2025
## R & LLM
- [Deep Dive into ellmer: Part 1](https://www.howardbaik.com/posts/deep-dive-into-ellmer-part1/)
I parsed through the source code of ellmer so you don’t have to


# 23.06.2025
## Визуализация нейронных сеток
- COOL! [netron](https://github.com/lutzroeder/netron): Visualizer for neural network, deep learning and machine learning models
- Keras
	- [Keras Visualizer](https://github.com/mahyar-amiri/keras-visualizer)
	- [Model plotting utilities](https://keras.io/api/utils/model_plotting_utils/)
- [torchview](https://github.com/mert-kurttutan/torchview): visualize pytorch models
Для пайторча - torchviz и torchviz2, но они рисуют излишне детализированное представление (ок для дебага, не ок для презентации)
