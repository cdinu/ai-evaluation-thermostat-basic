"""Model suites to run the thermostat eval against, via OpenRouter.

Model IDs are OpenRouter slugs (without the `openrouter/` prefix that Inspect
AI needs). They were checked against the OpenRouter model catalog on
2026-10-20. Labs ship new versions often, so refresh these lists when you
rerun the suite.
"""

# Latest flagship or widely used model from each major lab.
POPULAR = [
    "anthropic/claude-opus-5",
    "anthropic/claude-sonnet-5",
    "openai/gpt-5.5",
    "google/gemini-3.1-pro-preview",
    "google/gemini-3.5-flash",
    "x-ai/grok-4.6",
    "deepseek/deepseek-v4-flash",
    "moonshotai/kimi-k3",
    "z-ai/glm-5.2",
    "mistralai/mistral-large-2512",
    "qwen/qwen3-235b-a22b-thinking-2507",
]

# Free (`:free`) models that support tool calling. Free tiers are rate-limited,
# so run this suite with a low --max-tasks.
FREE = [
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
    "google/gemma-4-31b-it:free",
    "minimax/minimax-m3.1-flash:free",
    "thinkingmachines/inkling:free",
    "poolside/laguna-s-2.1:free",
    "xingchen-agi/xing4.0-29b-a4b:free",
    "dots-studio/dots-3-note-preview:free",
]

# The cheapest closed-weight commercial model from each major US, EU and
# Chinese provider: the kind of model a team reaches for to save money. Open-
# weight models are excluded, and so are batch endpoints. Ranked by prompt +
# completion price per token.
CHEAP = [
    # US
    "openai/gpt-5-nano",
    "anthropic/claude-haiku-5.5",
    "google/gemini-2.5-flash-lite",
    "x-ai/grok-build-0.1",
    # EU
    "mistralai/mistral-medium-3.1",
    # Chinese
    "qwen/qwen3.7-flash",
    "bytedance-seed/seed-1.6-flash",
    "z-ai/glm-5.3-flashx",
]

SUITES = {
    "popular": POPULAR,
    "free": FREE,
    "cheap": CHEAP,
    "all": POPULAR + FREE + CHEAP,
}
