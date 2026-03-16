#!/usr/bin/env python3
"""
Cookie Policy Template Generator (FR)
Generates a basic GDPR/CNIL-compliant cookie policy template in French.
"""
import sys
import argparse

def generate_policy(company_name, website_url, contact_email):
    """
    Generate a basic cookie policy template.
    """
    template = f"""# Politique d'Utilisation des Cookies

**Dernière mise à jour : [Date]**

La présente Politique d'Utilisation des Cookies explique comment **{company_name}** (« nous », « notre », ou « nos ») utilise les cookies et technologies similaires pour vous reconnaître lorsque vous visitez notre site web à l'adresse **{website_url}** (« le Site »).

## 1. Que sont les cookies ?
Les cookies sont de petits fichiers texte placés sur votre ordinateur ou appareil mobile lorsque vous visitez un site web. Ils sont largement utilisés pour faire fonctionner les sites web, ou les faire fonctionner plus efficacement, ainsi que pour fournir des informations aux propriétaires du site.

## 2. Pourquoi utilisons-nous des cookies ?
Nous utilisons des cookies de première partie et de tiers pour plusieurs raisons. Certains cookies sont nécessaires pour des raisons techniques afin que nos Sites fonctionnent : nous les appelons des cookies « strictement nécessaires » ou « essentiels ».

## 3. Les types de cookies que nous utilisons
- **Cookies strictement nécessaires :** Ces cookies sont indispensables pour vous permettre de naviguer sur le Site et d'utiliser ses fonctionnalités.
- **Cookies de performance et d'analyse :** Ces cookies recueillent des informations sur la manière dont les visiteurs utilisent un site web (par exemple, Google Analytics).
- **Cookies de fonctionnalité :** Ces cookies permettent au Site de se souvenir des choix que vous faites (comme votre nom d'utilisateur ou votre langue).
- **Cookies de ciblage / publicité :** Ces cookies sont utilisés pour diffuser des annonces plus pertinentes pour vous.

## 4. Comment pouvez-vous contrôler les cookies ?
Vous avez le droit de décider d'accepter ou de refuser les cookies. Vous pouvez exercer vos préférences en matière de cookies via notre bandeau de consentement lors de votre première visite, ou en modifiant les paramètres de votre navigateur.

## 5. Mises à jour de cette politique
Nous pouvons mettre à jour cette Politique d'Utilisation des Cookies de temps à autre pour refléter, par exemple, des changements dans les cookies que nous utilisons ou pour d'autres raisons opérationnelles, légales ou réglementaires.

## 6. Où obtenir de plus amples informations ?
Si vous avez des questions sur notre utilisation des cookies ou d'autres technologies, veuillez nous contacter par email à : **{contact_email}**
"""
    print(template)

def main():
    parser = argparse.ArgumentParser(description="Générateur de modèle de politique de cookies (FR)")
    parser.add_argument("--company", required=True, help="Nom de l'entreprise")
    parser.add_argument("--url", required=True, help="URL du site web")
    parser.add_argument("--email", required=True, help="Email de contact pour la confidentialité")

    args = parser.parse_args()
    generate_policy(args.company, args.url, args.email)

if __name__ == "__main__":
    main()
