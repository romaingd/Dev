<?php
$mot_de_passe_stocke = "";
$nonce_mot_de_passe;

$cle_secrete = random_bytes(SODIUM_CRYPTO_SECRETBOX_KEYBYTES);

stocker_mot_de_passe("monMot2Passe");

test_verifier_mot_de_passe("monMot2Passe"); // doit afficher "mot de passe valide"

test_verifier_mot_de_passe("autreMot2Passe"); // doit afficher "mot de passe invalide"

changer_mot_de_passe("autreMot2Passe"); // doit afficher "changement de mot de passe valide"

test_verifier_mot_de_passe("autreMot2Passe"); // doit afficher "mot de passe valide"

changer_mot_de_passe("autreMot2Passe2"); // doit afficher "erreur, le nouveau mot de passe est trop proche de l ancien"

function stocker_mot_de_passe($mot_de_passe_en_clair)
{
    $mot_de_passe_hache = sodium_crypto_pwhash_str($mot_de_passe_en_clair, SODIUM_CRYPTO_PWHASH_OPSLIMIT_INTERACTIVE, SODIUM_CRYPTO_PWHASH_MEMLIMIT_INTERACTIVE);
    $GLOBALS["nonce_mot_de_passe"] = random_bytes(SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);
    $GLOBALS["mot_de_passe_stocke"] = sodium_crypto_secretbox($mot_de_passe_hache, $GLOBALS["nonce_mot_de_passe"], $GLOBALS["cle_secrete"]);
}

function test_verifier_mot_de_passe($mot_de_passe_fourni)
{
    if (verifier_mot_de_passe($mot_de_passe_fourni)) {
        echo "mot de passe valide" . PHP_EOL;
    } else {
        echo "mot de passe invalide" . PHP_EOL;
    }
}

function verifier_mot_de_passe($mot_de_passe_fourni)
{
    // à écrire 
}

function changer_mot_de_passe($mot_de_passe_fourni)
{
    // à écrire
}

?>
