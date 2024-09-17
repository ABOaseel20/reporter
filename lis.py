<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>دمج الاسم مع الصورة</title>
</head>
<body>
    <h1>تحميل صورتين وإضافة الاسم</h1>

    <!-- تحميل الصور -->
    <input type="file" id="portrait" accept="image/*">
    <input type="file" id="landscape" accept="image/*">
    <br><br>

    <!-- إدخال الاسم -->
    <label for="name">أدخل الاسم:</label>
    <input type="text" id="name">
    <br><br>

    <!-- زر تنفيذ -->
    <button onclick="addNameToImages()">إضافة الاسم وتحميل الصورة</button>

    <!-- منطقة عرض الصور -->
    <canvas id="canvas" style="display:none;"></canvas>

    <script>
        function addNameToImages() {
            const portraitInput = document.getElementById('portrait').files[0];
            const landscapeInput = document.getElementById('landscape').files[0];
            const name = document.getElementById('name').value;
            const canvas = document.getElementById('canvas');
            const ctx = canvas.getContext('2d');

            if (!portraitInput || !landscapeInput || !name) {
                alert('يرجى تحميل الصور وإدخال الاسم');
                return;
            }

            // قراءة الصورة الطولية
            const readerPortrait = new FileReader();
            readerPortrait.onload = function(event) {
                const imgPortrait = new Image();
                imgPortrait.onload = function() {
                    canvas.width = imgPortrait.width;
                    canvas.height = imgPortrait.height;

                    // رسم الصورة الطولية
                    ctx.drawImage(imgPortrait, 0, 0);

                    // إضافة النص إلى الصورة
                    ctx.font = "30px Arial";
                    ctx.fillStyle = "white";
                    ctx.textAlign = "center";
                    ctx.fillText(name, canvas.width / 2, canvas.height - 30);

                    // تحميل الصورة
                    const link = document.createElement('a');
                    link.download = 'portrait_with_name.png';
                    link.href = canvas.toDataURL();
                    link.click();
                };
                imgPortrait.src = event.target.result;
            };
            readerPortrait.readAsDataURL(portraitInput);
        }
    </script>
</body>
</html>












