# Cross Resonance

some text

$$
\hat{H}^{CR}_{eff} = -\frac{\Delta_{12}}{2} \sigma^{z}_{1} + \frac{\Omega(t)}{2} \left(\sigma_2^x - \frac{J}{2\Delta_{12}} \sigma_1^z \sigma_2^x \right),
$$

n addition to understanding these extra terms, since the transmon has higher energy levels and actual experiments may have other interactions, due to crosstalk for example, when applying an entangling operation, it is not always obvious which Pauli rotations will be generated. Here we assume a cross resonance Hamiltonian of the following form:

$$
\begin{align}
\hat{H}
= \frac{\hat{Z} \otimes \hat{A}}{2} + \frac{\hat{I} \otimes \hat{B}}{2}
= a_{x} \hat{Z}\hat{X} + a_{y} \hat{Z}\hat{Y} + a_{z} \hat{Z}\hat{Z} + b_{x}  \hat{I}\hat{X} + b_{y} \hat{I}\hat{Y} + b_{z} \hat{I}\hat{Z}
\end{align}
$$

, where $\hat{Z}\hat{X} = \hat{Z} \otimes \hat{X} = \sigma_1^z \otimes \sigma_2^x = \sigma_1^z \sigma_2^x$.

$$
\begin{align}
\langle \hat{O}(t) \rangle = \langle e^{i\hat{H}t} \hat{O} e^{-i\hat{H}t} \rangle
\end{align}
$$

and more

$$
\begin{align}
a^\dagger_1 &= \frac{X - iY}{2} \otimes I \otimes I \otimes ... \otimes I \\
a^\dagger_2 &= Z \otimes \frac{X - iY}{2} \otimes I \otimes ... \otimes I \\
&\vdots \\
a^\dagger_{2n} &= Z \otimes Z \otimes Z \otimes ... \otimes \frac{X -iY}{2}
\end{align}
$$

and more

$$
\begin{align}
&\left[\hat{H}, \hat{I}\hat{X}\right] = 2 i \left(a_{y} \hat{Z}\hat{Z} - a_{z} \hat{Z}\hat{Y} + b_{y} \hat{I}\hat{Z} - b_{z} \hat{I}\hat{Y}\right) \\
&\left[\hat{H},\hat{I}\hat{Y}\right] = 2 i \left(-a_{x} \hat{Z}\hat{Z} + a_{z} \hat{Z}\hat{X} - b_{x} \hat{I}\hat{Z} + b_{z} \hat{I}\hat{X}\right)\\
&\left[\hat{H}, \hat{I}\hat{Z}\right] = 2 i \left(a_{x} \hat{Z}\hat{Y} - a_{y} \hat{Z}\hat{X} + b_{x} \hat{I}\hat{Y} - b_{y} \hat{I}\hat{X}\right)
\end{align}
$$

and more

$$
\begin{align}
i\langle\left[\hat{H},\hat{I}\hat{X} \right]\rangle_{\rm control} &= 2 \left(n a_{z} + b_{z}\right)\langle\hat{Y}\rangle - 2 \left(n a_{y} + b_{y}\right)\langle\hat{Z}\rangle \\
i\langle\left[\hat{H}, \hat{I}\hat{Y}\right]\rangle_{\rm control} &= 2\left(n a_{x} + b_{x}\right) \langle\hat{Z}\rangle-2 \left(n a_{z} + b_{z}\right) \langle\hat{X}\rangle \\
i\langle\left[\hat{H}, \hat{I}\hat{Z}\right]\rangle_{\rm control} &= 2 \left(n a_{y} + b_{y}\right) \langle\hat{X}\rangle - 2 \left(n a_{x} + b_{x}\right) \langle\hat{Y}\rangle
\end{align}
$$

and more

$$
\begin{align}
\langle \hat{X}(t) \rangle_n &= \frac{1}{\Omega^2}\left(-\Delta \Omega_x + \Delta\Omega_x\cos(\Omega t) + \Omega \Omega_y \sin(\Omega t)\right) \\
\langle \hat{Y}(t) \rangle_n &= \frac{1}{\Omega^2}\left(\Delta \Omega_y - \Delta\Omega_y\cos(\Omega t) - \Omega \Omega_x \sin(\Omega t)\right) \\
\langle \hat{Z}(t) \rangle_n &= \frac{1}{\Omega^2}\left(\Delta^2 + \left(\Omega_x^2+\Omega_y^2\right)\cos(\Omega t) \right)
\end{align}
$$

$$
\begin{align}
\end{align}
$$

$$
\begin{align}
\end{align}
$$

$$
\begin{align}
\end{align}
$$

$$
\begin{align}
\end{align}
$$

# CNOT
