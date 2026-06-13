document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-message-dismiss]').forEach((button) => {
        button.addEventListener('click', () => {
            const message = button.closest('.message');
            if (message) {
                message.remove();
            }
        });
    });

    const contentField = document.getElementById('id_content');
    const counter = document.querySelector('[data-content-counter]');

    if (contentField && counter) {
        const updateCounter = () => {
            const length = contentField.value.trim().length;
            counter.textContent = `${length} char${length === 1 ? '' : 's'}`;
        };

        contentField.addEventListener('input', updateCounter);
        updateCounter();
    }

    const copyButton = document.querySelector('[data-copy-note]');
    if (copyButton) {
        copyButton.addEventListener('click', async () => {
            const title = copyButton.getAttribute('data-copy-title') || '';
            const content = copyButton.getAttribute('data-copy-content') || '';
            const text = [title, content].filter(Boolean).join('\n\n');

            try {
                await navigator.clipboard.writeText(text);
                copyButton.textContent = 'Copied';
                window.setTimeout(() => {
                    copyButton.textContent = 'Copy text';
                }, 1400);
            } catch (error) {
                copyButton.textContent = 'Copy failed';
                window.setTimeout(() => {
                    copyButton.textContent = 'Copy text';
                }, 1400);
            }
        });
    }

    const deleteForm = document.querySelector('[data-delete-form]');
    if (deleteForm) {
        deleteForm.addEventListener('submit', (event) => {
            const confirmed = window.confirm('Delete this note permanently?');
            if (!confirmed) {
                event.preventDefault();
            }
        });
    }
});