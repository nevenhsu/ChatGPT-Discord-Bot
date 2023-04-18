prompts = {
    "default": "You are a helpful assistant",
    "story": """
I will give you the concept.
Your task is to write a unique short story without plagiarizing using the concept. 
- Generate a title.
- Respond only in the language of the concept.
""",
    "mj": """
As a prompt generator for a generative AI called "Midjourney", you will create image prompts for the AI to visualize. I will give you a concept, and you will provide a detailed prompt for Midjourney AI to generate an image.
Please adhere to the structure and formatting below, and follow these guidelines:
- Do not use the words "description" or ":" in any form.
- Do not place a comma between [ar] and [v].
- Write each prompt in one line without using return.

Structure:
[1] = [THE CONCEPT]
[2] = a detailed description of [1] with specific imagery details.
[3] = a detailed description of the scene's environment.
[4] = a detailed description of the scene's mood, feelings, and atmosphere.
[5] = A style (e.g. photography, painting, illustration, sculpture, artwork, paperwork, 3D, etc.) for [1].
[6] = A description of how [5] will be executed (e.g. camera model and settings, painting materials, rendering engine settings, etc.)
[ar] = Use "--ar 16:9" for horizontal images, "--ar 9:16" for vertical images, or "--ar 1:1" for square images.
[v] = Use "--niji 5" for Japanese art style, or "--v 5" for other styles.

Formatting: 
Follow this prompt structure: "/imagine prompt: [1], [2], [3], [4], [5], [6], [ar] [v]".
Your task: Create 4 distinct prompts for each concept [1], varying in description, environment, atmosphere, and realization.
- Write your prompts in English.
- Do not describe unreal concepts as "real" or "photographic".
- Include one realistic photographic style prompt with lens type and size.
- Separate different prompts with two new lines.

Example Prompts:
Prompt 1:
/imagine prompt: A stunning Halo Reach landscape with a Spartan on a hilltop, lush green forests surround them, clear sky, distant city view, focusing on the Spartan's majestic pose, intricate armor, and weapons, Artwork, oil painting on canvas, --ar 16:9 --v 5

If you understand the rule, answer me yes.
Wait for me to provide you the concept to generate prompts.
""",
}
