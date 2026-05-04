
Dyekiss Gábor Emil shared "Quiz 3" with you

Dyekiss Gábor Emil
​hyojeong.seok@student.hanken.fi​
Share image

Dyekiss Gábor Emil shared a file with you

Here's the document that Dyekiss Gábor Emil shared with you.
icon 	Quiz 3
permission globe icon 	This link only works for the direct recipients of this message.
Open

This email is generated through Corvinus University of Budapest's use of Microsoft 365 and may contain content that is controlled by Corvinus University of Budapest.
Hyojeong Seok<hyojeong.seok@student.hanken.fi>
​Dyekiss Gábor Emil​
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Performance-Based Budgeting in Indonesia - Hyojeong Seok</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
       
        body { font-family: 'Inter', sans-serif; background-color: #f3f4f6; margin: 0; overflow: hidden; }
        .slide { display: none; height: 100vh; width: 100vw; padding: 3rem; box-sizing: border-box; background: linear-gradient(135deg, #ffffff 0%, #f9fafb 100%); }
        .slide.active { display: flex; flex-direction: column; }
        .title-slide { background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; justify-content: center; align-items: center; text-align: center; }
        .content-header { border-bottom: 3px solid #3b82f6; margin-bottom: 2rem; padding-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center; }
        .content-body { flex-grow: 1; font-size: 1.25rem; line-height: 1.6; }
        .card { background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 5px solid #3b82f6; }
        .progress-bar { position: fixed; bottom: 0; left: 0; height: 5px; background-color: #3b82f6; transition: width 0.3s ease; }
        .controls { position: fixed; bottom: 20px; right: 20px; display: flex; gap: 10px; z-index: 100; }
        .control-btn { background: rgba(0,0,0,0.1); border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; }
        .gemini-btn { background: linear-gradient(to right, #8e2de2, #4a00e0); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; display: flex; align-items: center; gap: 0.5rem; }
       
        /* Sidebar for Gemini Responses */
        #aiSidebar {
            position: fixed; top: 0; right: -400px; width: 400px; height: 100%; background: white;
            box-shadow: -2px 0 10px rgba(0,0,0,0.1); transition: right 0.3s; z-index: 1001; padding: 2rem;
            display: flex; flex-direction: column;
        }
        #aiSidebar.open { right: 0; }
        .loading { display: none; }
        .loading.active { display: block; }
    </style>
</head>
<body>
    <div class="progress-bar" id="progressBar"></div>

    <div id="aiSidebar">
        <div class="flex justify-between items-center mb-4">
            <h3 class="font-bold text-purple-700">✨ Gemini AI Assistant</h3>
            <button onclick="toggleAI()"><i class="fas fa-times"></i></button>
        </div>
        <div id="aiLoading" class="loading mb-4 text-purple-600 font-bold">Thinking...</div>
        <div id="aiResponse" class="overflow-y-auto text-sm leading-relaxed whitespace-pre-wrap"></div>
    </div>

    <!-- Slides -->
    <div class="slide active title-slide">
        <h1 class="text-5xl font-bold mb-6">Performance-Based Budgeting in Indonesia</h1>
        <button onclick="askAI('Create a 30-second opening script for this slide in English')" class="gemini-btn">✨ Generate Script</button>
    </div>

    <div class="slide">
        <div class="content-header">
            <h2 class="text-3xl font-bold text-blue-900">1. Introduction</h2>
            <button onclick="askAI('Explain why 2003 was a significant year for Indonesian finance in 2 sentences')" class="gemini-btn">✨ Explain History</button>
        </div>
        <div class="content-body">
            <div class="card">
                <p><strong>Background:</strong> Significant reforms initiated in 2003 to combat corruption and improve efficiency via Act No. 17 of 2003.</p>
            </div>
        </div>
    </div>

    <!-- Controls -->
    <div class="controls">
        <button class="control-btn" onclick="prevSlide()"><i class="fas fa-chevron-left"></i></button>
        <button class="control-btn" onclick="nextSlide()"><i class="fas fa-chevron-right"></i></button>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const sidebar = document.getElementById('aiSidebar');
        const responseDiv = document.getElementById('aiResponse');
        const loadingDiv = document.getElementById('aiLoading');
        const apiKey = "";

        function toggleAI() { sidebar.classList.toggle('open'); }

        async function askAI(prompt) {
            toggleAI();
            loadingDiv.classList.add('active');
            responseDiv.innerText = "";
           
            try {
                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] })
                });
                const data = await response.json();
                responseDiv.innerText = data.candidates[0].content.parts[0].text;
            } catch (e) {
                responseDiv.innerText = "Error calling AI. Please check connectivity.";
            } finally {
                loadingDiv.classList.remove('active');
            }
        }

        function updateSlide() {
            slides.forEach((s, i) => s.classList.toggle('active', i === currentSlide));
            document.getElementById('progressBar').style.width = ((currentSlide + 1) / slides.length * 100) + '%';
        }

        function nextSlide() { if (currentSlide < slides.length - 1) { currentSlide++; updateSlide(); } }
        function prevSlide() { if (currentSlide > 0) { currentSlide--; updateSlide(); } }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
        });
    </script>
</body>
</html>
