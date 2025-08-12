import numpy as np
import sys

def main():
    if sys.argv[1][-5:] == '.lmps':
        input_f = sys.argv[1]
        output_f = input_f[:-5] + '.cssr'
    else:
        raise ValueError('input file should be a .lmps file')
    structure_name = sys.argv[2]

    with open(input_f, 'r') as f:
        lines = f.readlines()

    masses_flag = False
    atom_types = [0]
    for line in lines[:80]:
        if 'xlo' in line:
            vals = line.split()
            x_len = float(vals[1]) - float(vals[0])
        if 'ylo' in line:
            vals = line.split()
            y_len = float(vals[1]) - float(vals[0])
        if 'zlo' in line:
            vals = line.split()
            z_len = float(vals[1]) - float(vals[0])
        if 'atoms\n' in line:
            num_atoms = line.split()[0]
        if 'Masses\n' in line:
            masses_flag = True
        if 'Bond Coeffs' in line:
            masses_flag = False
        if masses_flag and line != '\n' and 'Masses' not in line:
            curr_type = line.split()[3]
            print('curr_type ' + curr_type)
            if curr_type[1:2] == '_':
                atom_types.append(curr_type[0:1])
            else:
                atom_types.append(curr_type[0:2])

    print('Header info read')

    with open(output_f, 'w') as f:
        # Writing .cssr header
        f.write(str(x_len) + '  ' + str(y_len) + '  ' + str(z_len) + '\n')
        #Assume 90 degree angles, and assume P1 symmetry
        f.write('90  90  90  SPGR =  1 P 1\n')
        f.write(num_atoms + '  0\n')
        f.write('0  ' + structure_name + '\n')

        atoms_flag = False
        for line in lines:
            if 'Atoms' in line:
                atoms_flag = True
            if 'Velocit' in line or 'Bonds' in line:
                atoms_flag = False
            if atoms_flag and line != '\n' and 'Atoms' not in line:
                vals = line.split()
                # Writing .cssr body (atom info, with nine trailing zeros)
                f.write(vals[0] + ' ')
                f.write(atom_types[int(vals[2])] + ' ')
                f.write(str(float(vals[4])/x_len) + ' ')
                f.write(str(float(vals[5])/y_len) + ' ')
                f.write(str(float(vals[6])/z_len) + ' ')
                f.write('0  0  0  0  0  0  0  0  0.0')
                f.write('\n')

if __name__ == '__main__':
    main()
    print('Finished')
