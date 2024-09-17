document.addEventListener("DOMContentLoaded", function() {
    // مثال لتحميل الصور بشكل كسول
    const lazyImages = document.querySelectorAll('img[loading="lazy"]');
    lazyImages.forEach(img => {
        img.src = img.dataset.src;
    });

    // إضافة تأثير تفاعل بسيط عند تمرير الفأرة على عناصر القائمة
    const sheepItems = document.querySelectorAll('.sheep-item');
    sheepItems.forEach(item => {
        item.addEventListener('mouseover', () => {
            item.style.transform = 'scale(1.05)';
        });
        item.addEventListener('mouseout', () => {
            item.style.transform = 'scale(1)';
        });
    });
});