/**
 * Script para extração de links de vídeos, shorts e lives do YouTube.
 * Deve ser executado no console do navegador (browser_console_exec).
 */

async function collectLinks(type = 'videos') {
    let links = new Set();
    let lastCount = 0;
    let retries = 0;
    
    // Define o seletor com base no tipo de conteúdo
    let selector = 'a#video-title-link, a#video-title';
    if (type === 'shorts') {
        selector = 'a[href^="/shorts/"]';
    }

    for (let i = 0; i < 15; i++) {
        window.scrollTo(0, document.documentElement.scrollHeight);
        await new Promise(r => setTimeout(r, 2000));
        
        let currentElements = document.querySelectorAll(selector);
        currentElements.forEach(el => {
            if (el.href) {
                let url = el.href.split("&")[0].split("?")[0];
                // Filtra links genéricos de shorts
                if (url !== "https://www.youtube.com/shorts/") {
                    links.add(url);
                }
            }
        });

        if (links.size === lastCount) {
            retries++;
        } else {
            retries = 0;
            lastCount = links.size;
        }
        
        // Se não encontrar novos links após 3 rolagens, para
        if (retries > 3) break;
    }
    
    return Array.from(links);
}

// O tipo pode ser passado como argumento se necessário, padrão é 'videos'
return await collectLinks();
