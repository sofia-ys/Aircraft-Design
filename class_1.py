# class 1 estimations
# comment 2
import numpy as nmp
import matplotlib.pyplot as mtplt

max_payload = nmp.array([25970, 41050, 18711, 23133, 18325, 22000, 62250, 23000, 16150, 40000, 33355])
MTOM = nmp.array([115680, 228000, 70896, 87997, 141521, 186880, 273310, 165000, 61500, 250000, 211374])
max_range = nmp.array([7222, 13530, 6300, 7408, 8112, 11305, 12270, 8000, 4815, 10000, 6862])
OEM = nmp.array([58390, 119950, 37080, 45450, 66670, 90770, 132800, 74000, 33300, 120400, 111795])

def estimate_coeff(p, q):
    # Here, we will estimate the total number of points or observation
    n1 = nmp.size(p)
    # Now, we will calculate the mean of a and b vector
    m_p = nmp.mean(p)
    m_q = nmp.mean(q)

    # here, we will calculate the cross deviation and deviation about a
    SS_pq = nmp.sum(q * p) - n1 * m_q * m_p
    SS_pp = nmp.sum(p * p) - n1 * m_p * m_p

    # here, we will calculate the regression coefficients
    b_1 = SS_pq / SS_pp
    b_0 = m_q - b_1 * m_p

    return (b_0, b_1)


def plot_regression_line(p, q, b):
    # Now, we will plot the actual points or observation as scatter plot
    mtplt.scatter(p, q, color="m",
                  marker="o", s=30)

    # here, we will calculate the predicted response vector
    q_pred = b[0] + b[1] * p

    # here, we will plot the regression line
    mtplt.plot(p, q_pred, color="g")

    # here, we will put the labels
    mtplt.xlabel('p')
    mtplt.ylabel('q')

    # here, we will define the function to show plot
    mtplt.show()


def main(p, q):
    # now, we will estimate the coefficients
    b = estimate_coeff(p, q)
    print("Estimated coefficients are :\nb_0 = {} \
    \nb_1 = {}".format(b[0], b[1]))

    # Now, we will plot the regression line
    plot_regression_line(p, q, b)

    if __name__ == "__main__":
        main()
main(OEM, max_payload)