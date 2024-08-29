add_cus_dep('glo', 'gls', 0, 'makeglossaries');
add_cus_dep('acn', 'acr', 0, 'makeglossaries');

sub makeglossaries {
    system("makeglossaries -d .build main");
    return 0;
}

$bibtex_use = 1;
$aux_dir = '.build';  # Set the auxiliary directory to .build
$out_dir = '.build';  # Set the output directory to .build
$clean_ext .= ' %R.glg %R.glo %R.gls %R.alg %R.acn %R.acr %R.blg';
