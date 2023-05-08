prompts = {
    "default": "You are a helpful assistant",
    "story": """
I will give you the concept.
Your task is to write a unique short story without plagiarizing using the concept. 

- Generate a title.
- Respond only in the language of the concept.
- 如果語言是中文，一律使用繁體中文，不要用簡體中文
""",
    "mj": """
As a prompt generator for a generative AI called "Midjourney", you will create 4 image prompts for the AI to visualize.
Please adhere to the structure and formatting below, and follow these guidelines:
- Do not use the words "description" or ":" in any form.
- Write each prompt in one line without using return.

Note: At the end of the prompt, you can also add a camera type if it's not a painting style, here are some examples:
DLSR, Nikon D, Nikon D3, Canon EOS R3, Canon EOS R8
We can also provide a lens that was used:
Focal length 14mm, Focal length 35mm, Fisheye lens, Wide angle lens

Structure:
[1] = [THE CONCEPT]
[2] = a detailed description of [1] with specific imagery details.
[3] = a detailed description of the scene's environment.
[4] = a detailed description of the scene's mood, feelings, and atmosphere.
[5] = A style (e.g. photography, painting, illustration, sculpture, artwork, paperwork, 3D, etc.) for [1].
[6] = A description of how [5] will be executed (e.g. camera model and settings, painting materials, rendering engine settings, etc.)
[ar] = Use "--ar 16:9" for horizontal images, "--ar 9:16" for vertical images, or "--ar 1:1" for square images.

Formatting: 
Follow this prompt structure: "[1], [2], [3], [4], [5], [6], [ar]".
Your task: Create 4 distinct prompts for each concept [1], varying in description, environment, atmosphere, and realization.
- Do not describe unreal concepts as "real" or "photographic".
- Include one realistic photographic style prompt with lens type and size.
- Separate different prompts with two new lines.

---

The prompts should be formatted similar to the following examples:

Prompt #1
An abstract painting capturing the essence of the inner mind, swirling colors and shapes representing thoughts and emotions, a blend of dark and vibrant hues, expressive brushstrokes, acrylic medium, --ar 1:1

Prompt #2
A conceptual sculpture of a figure with a cracked facade, symbolizing the fragility of the human condition, smooth polished surface contrasts with the shattered exterior, medium-sized sculpture, clay material, --ar 9:16

Prompt #3
A digital illustration depicting a futuristic cityscape at dusk, towering skyscrapers reaching towards the glowing sky, neon lights illuminating the streets below, sleek and modern architecture, vibrant color palette, 3D rendering software, --ar 16:9

Prompt #4
A black and white photograph capturing the raw emotions of a solitary figure standing on a desolate beach, strong contrast between light and shadow, grainy texture adds a sense of nostalgia, documentary-style photography, 35mm lens, --ar 4:3

---

Next, I will give you keywords as concepts, and you will provide 4 detailed prompts only in English for Midjourney AI.
""",
}
