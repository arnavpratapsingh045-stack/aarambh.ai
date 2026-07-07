<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aarambh AI</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .chat-container::-webkit-scrollbar {
            width: 6px;
        }
        .chat-container::-webkit-scrollbar-thumb {
            background-color: #4b5563;
            border-radius: 10px;
        }
    </style>
</head>
<body class="bg-gray-950 text-gray-100 font-sans h-screen flex flex-col justify-between m-0">

    <div id="auth-screen" class="fixed inset-0 bg-gray-900 z-50 flex flex-col items-center justify-center p-4">
        <div class="bg-gray-800 p-8 rounded-2xl shadow-2xl max-w-md w-full text-center border border-gray-700">
            <h1 class="text-4xl font-extrabold text-blue-500 mb-2 tracking-wider">AARAMBH AI</h1>
            <p class="text-gray-400 mb-8 text-sm">The Next Generation AI Platform</p>
            
            <div class="mb-6">
                <label class="block text-left text-sm font-medium text-gray-300 mb-2">आपका नाम / Your Name</label>
                <input type="text" id="user-name-input" placeholder="Enter your name..." value="Arnav Partap Singh" class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-white">
            </div>

            <button onclick="handleLogin()" class="w-full flex items-center justify-center gap-3 bg-white text-gray-900 font-semibold py-3 px-4 rounded-lg hover:bg-gray-200 transition duration-300 shadow-lg cursor-pointer">
                <svg class="w-5 h-5" viewBox="0 0 24 24">
                    <path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v3.92h6.69c-.29 1.5-.1.14-1.14 2.84v2.35h3.31c1.93-1.78 3.04-4.4 3.04-7.44z"/>
                    <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.31-2.35c-.92.62-2.11 1-3.62 1-3.11 0-5.74-2.11-6.68-4.96H2.96v2.42C4.94 21.14 8.23 24 12 24z"/>
                    <path fill="#FBBC05" d="M5.32 14.78c-.24-.72-.38-1.49-.38-2.28s.14-1.56.38-2.28V7.8H2.96C2.15 9.42 1.69 11.24 1.69 13s.46 3.58 1.27 5.2h2.36l-.38-3.42z"/>
                    <path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.44-3.44C17.93 1.19 15.24 0 12 0 8.23 0 4.94 2.86 2.96 6.58l3.36 2.42c.94-2.85 3.57-4.96 6.68-4.96z"/>
                </svg>
                Continue with Google Email
            </button>
        </div>
    </div>

    <header class="bg-gray-900 border-b border-gray-800 px-6 py-4 flex justify-between items-center shadow-md">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center font-bold text-xl tracking-wider shadow-lg shadow-blue-500/20">A</div>
            <div>
                <h2 class="text-lg font-bold text-white tracking-wide">Aarambh Engine</h2>
                <p id="welcome-tag" class="text-xs text-green-400 font-medium"></p>
            </div>
        </div>
        <div class="text-xs bg-gray-800 text-gray-400 px-3 py-1.5 rounded-full border border-gray-700">
            <span class="inline-block w-2 h-2 bg-green-500 rounded-full mr-1.5 animate-pulse"></span> Active v1.0
        </div>
    </header>

    <main id="chat-box" class="chat-container flex-1 overflow-y-auto p-6 space-y-6 max-w-4xl w-full mx-auto flex flex-col">
        <div class="flex gap-4 items-start max-w-[85%]">
            <div class="w-8 h-8 rounded-lg bg-blue-600 flex items-center justify-center text-xs font-bold shrink-0">AI</div>
            <div class="bg-gray-800 p-4 rounded-2xl rounded-tl-none border border-gray-700 text-gray-200 shadow-sm leading-relaxed">
                नमस्ते! मैं **Aarambh AI** हूँ। मैं दुनिया की सभी भाषाएं समझ और बोल सकता हूँ। मैं आपकी क्या मदद कर सकता हूँ?
            </div>
        </div>
    </main>

    <footer class="bg-transparent pb-6 px-4">
        <div class="max-w-4xl mx-auto bg-gray-900 rounded-2xl border border-gray-800 shadow-2xl p-3">
            <div class="flex items-center gap-3">
                
                <label for="photo-upload" class="flex items-center justify-center w-11 h-11 bg-gray-800 hover:bg-gray-700 text-gray-300 rounded-xl cursor-pointer transition duration-200 border border-gray-700">
                    <i class="fa-solid fa-plus text-lg"></i>
                    <input type="file" id="photo-upload" accept="image/*" class="hidden" onchange="handleImageUpload(event)">
                </label>

                <input type="text" id="user-input" placeholder="Ask Aarambh Engine anything... (Type in any language)" class="flex-1 bg-transparent border-0 text-white placeholder-gray-500 py-3 px-2 focus:outline-none focus:ring-0 text-base" onkeydown="if(event.key === 'Enter') sendMessage()">

                <button onclick="startVoiceRecognition()" class="flex items-center justify-center w-11 h-11 bg-gray-800 hover:bg-gray-700 text-gray-300 rounded-xl transition duration-200 border border-gray-700 cursor-pointer" title="Voice Input">
                    <i class="fa-solid fa-microphone text-lg" id="mic-icon"></i>
                </button>

                <button onclick="sendMessage()" class="flex items-center justify-center w-11 h-11 bg-blue-600 hover:bg-blue-500 text-white rounded-xl transition duration-200 shadow-lg shadow-blue-600/30 cursor-pointer">
                    <i class="fa-solid fa-paper-plane text-sm"></i>
                </button>
            </div>
        </div>
    </footer>

    <script>
        let currentUserName = "User";

        // Point 1 & 2: Handling Login and Setting welcome text
        function handleLogin() {
            const nameInput = document.getElementById('user-name-input').value.trim();
            if(nameInput !== "") {
                currentUserName = nameInput;
            }
            document.getElementById('welcome-tag').innerText = `Welcome ${currentUserName}`;
            document.getElementById('auth-screen').classList.add('hidden');
        }

        // Handle Image Upload UI Feedback
        function handleImageUpload(event) {
            const file = event.target.files[0];
            if (file) {
                appendMessage(`[Photo Selected: ${file.name}]`, true);
                // Simulated AI Response for image upload
                setTimeout(() => {
                    appendMessage("मैंने आपकी फोटो देख ली है। Aarambh Engine इसे प्रोसेस कर रहा है।", false);
                }, 1000);
            }
        }

        // Point 5: Speech to Text (Mic Input Feature)
        function startVoiceRecognition() {
            const micIcon = document.getElementById('mic-icon');
            if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
                const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                const recognition = new SpeechRecognition();
                
                // Point 4 & 7: Setting it to listen to Hindi/Global multiple formats
                recognition.lang = 'hi-IN'; 
                recognition.interimResults = false;

                recognition.onstart = function() {
                    micIcon.classList.remove('fa-microphone');
                    micIcon.classList.add('fa-spinner', 'animate-spin', 'text-red-500');
                };

                recognition.onerror = function() {
                    resetMic();
                };

                recognition.onend = function() {
                    resetMic();
                };

                recognition.onresult = function(event) {
                    const speechToText = event.results[0][0].transcript;
                    document.getElementById('user-input').value = speechToText;
                };

                recognition.start();
            } else {
                alert("Your browser does not support Speech Recognition.");
            }
        }

        function resetMic() {
            const micIcon = document.getElementById('mic-icon');
            micIcon.classList.remove('fa-spinner', 'animate-spin', 'text-red-500');
            micIcon.classList.add('fa-microphone');
        }

        // Message Processing & Point 6 Rules (Identity Filter)
        function sendMessage() {
            const inputField = document.getElementById('user-input');
            const messageText = inputField.value.trim();
            
            if (messageText === "") return;

            // Append User Message to UI
            appendMessage(messageText, true);
            inputField.value = "";

            // Auto-scroll
            const chatBox = document.getElementById('chat-box');
            chatBox.scrollTop = chatBox.scrollHeight;

            // Processing AI Response with Rules
            setTimeout(() => {
                let aiResponse = "";
                const cleanQuery = messageText.toLowerCase();

                // Point 6 Identity Guard: Hardcoded priority check
                if (cleanQuery.includes("kisne banaya") || cleanQuery.includes("who created") || cleanQuery.includes("who made you") || cleanQuery.includes("creator") || cleanQuery.includes("owner") || cleanQuery.includes("founder")) {
                    aiResponse = "मुझे **Alliance Group** के **AI Technology Team** ने बनाया है। और Alliance Group के CEO & Founder **Arnav Partap Singh** हैं।";
                } 
                // Point 8: Strict Anti-Gemini Branding filter
                else if (cleanQuery.includes("gemini") || cleanQuery.includes("google")) {
                    aiResponse = "मैं **Aarambh AI** हूँ, जिसे Aarambh Engine द्वारा संचालित किया जाता है। मेरा संबंध किसी अन्य ब्रांड से नहीं है।";
                }
                else {
                    // Standard Simulated Core Response (Point 4 & 7: Multilingual Reply flow)
                    aiResponse = `यह "Aarambh Engine" का एक मॉक रिस्पॉन्स है। जब आप इसमें बैकएंड API कनेक्ट करेंगे, तो यह आपके "${messageText}" का लाइव जवाब अनलिमिटेड चैट मोड में देगा।`;
                }

                appendMessage(aiResponse, false);
                chatBox.scrollTop = chatBox.scrollHeight;
            }, 800);
        }

        // Helper to Inject Chat Bubbles into UI
        function appendMessage(text, isUser) {
            const chatBox = document.getElementById('chat-box');
            const messageWrapper = document.createElement('div');
            messageWrapper.className = `flex gap-4 items-start ${isUser ? 'justify-end max-w-[85%] ml-auto' : 'max-w-[85%]'}`;

            const avatarHtml = isUser 
                ? `<div class="w-8 h-8 rounded-lg bg-gray-700 flex items-center justify-center text-xs font-bold shrink-0 uppercase">${currentUserName.substring(0,2)}</div>`
                : `<div class="w-8 h-8 rounded-lg bg-blue-600 flex items-center justify-center text-xs font-bold shrink-0">AI</div>`;

            const bubbleHtml = `
                <div class="${isUser ? 'bg-blue-600 text-white rounded-tr-none' : 'bg-gray-800 text-gray-200 rounded-tl-none border border-gray-700'} p-4 rounded-2xl shadow-sm leading-relaxed">
                    ${text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}
                </div>
            `;

            if (isUser) {
                messageWrapper.innerHTML = bubbleHtml + avatarHtml;
            } else {
                messageWrapper.innerHTML = avatarHtml + bubbleHtml;
            }

            chatBox.appendChild(messageWrapper);
        }
    </script>
</body>
</html>

