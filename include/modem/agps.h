/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
 */

/**
 * @file agps.h
 * @brief Public APIs for the A-GPS library.
 * @defgroup agps A-GPS library
 * @{
 */

#ifndef AGPS_H_
#define AGPS_H_

#include <stddef.h>
#include <stdint.h>

#include <nrf_modem_gnss.h>

#ifdef __cplusplus
extern "C" {
#endif

#define AGPS_SOCKET_NOT_PROVIDED 0

/**
 * @brief Function to send a request for A-GPS data to the configured A-GPS data source. See the
 *        A-GPS library Kconfig documentation for alternatives.
 *
 * @param request Assistance data to request from the A-GPS service.
 * @param socket GNSS socket to which assistance data will be written when it's received from the
 *               selected A-GPS service. If socket argument is set to AGPS_SOCKET_NOT_PROVIDED,
 *               the data will be written using the GPS driver or GNSS API.
 *
 * @return Zero on success or (negative) error code otherwise.
 */
int agps_request_send(struct nrf_modem_gnss_agps_data_frame request, int socket);

/**
 * @brief Processes A-GPS data from the cloud.
 *
 * @param buf Pointer to A-GPS data from the cloud.
 * @param len Buffer size of data to be processed.
 *
 * @return Zero on success or (negative) error code otherwise.
 */
int agps_cloud_data_process(const uint8_t *buf, size_t len);

/** @} */

#ifdef __cplusplus
}
#endif

#endif /* AGPS_H_ */
